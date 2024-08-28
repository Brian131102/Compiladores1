from flask import Flask, request, render_template, jsonify
import os
import ply.lex as lex

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Definición de tokens y analizador léxico
reserved = {
    'public': 'RESERVADO',
    'static': 'RESERVADO',
    'void': 'RESERVADO',
    'int': 'RESERVADO',
    'for': 'RESERVADO',
}

tokens = list(reserved.values()) + [
    'IDENTIFICADOR', 'DELIMITADOR', 'OPERADOR', 'NUMERO', 'SIMBOLO'
]

def t_DELIMITADOR(t):
    r'[\{\}\(\);,]'  # Captura llaves, paréntesis y otros delimitadores
    return t

def t_SIMBOLO(t):
    r'\.'  # Captura el símbolo de punto
    t.type = 'SIMBOLO'
    return t

def t_NUMERO(t):
    r'\d'  # Captura solo un dígito como número
    t.value = int(t.value)
    return t

def t_OPERADOR(t):
    r'='
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFICADOR')
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('error.html', file_error="No se ha enviado ningún archivo")

        file = request.files['file']

        if file.filename == '':
            return render_template('error.html', file_error="No se ha seleccionado ningún archivo")

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Leer el contenido del archivo y mostrarlo en el área de texto
        with open(file_path, 'r') as f:
            file_content = f.read()

        return render_template('home.html', file_content=file_content)

    return render_template('home.html')

@app.route("/analyze", methods=['POST'])
def analyze_code():
    try:
        code = request.json['code']
        lexer.input(code)
        tokens = []
        
        # Inicializar contadores
        counts = {
            'RESERVADO': 0,
            'IDENTIFICADOR': 0,
            'DELIMITADOR': 0,
            'OPERADOR': 0,
            'NUMERO': 0,
            'SIMBOLO': 0  # Contador para el token de símbolos (punto)
        }

        lexer.lineno = 1
        for tok in lexer:
            token_info = {
                'type': tok.type,
                'value': tok.value,
                'lineno': tok.lineno,
            }
            tokens.append(token_info)
            # Incrementar el contador correspondiente
            if tok.type in counts:
                counts[tok.type] += 1

        return jsonify({
            'tokens': tokens,
            'counts': counts
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)





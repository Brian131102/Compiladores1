import ply.lex as lex

# Definir los tokens para el analizador léxico
tokens = (
    'RESERVADA', 'PARIZQ', 'PARDER', 'IDENTIFICADOR', 'ASIGNAR', 'ENTERO', 'PUNTOCOMA', 'MENORIGUAL',
    'PLUSPLUS', 'LLAIZQ', 'LLADER', 'PUNTO', 'COMDOB', 'DOSPUNTO', 'SUMA', 'MENOS'
)

# Expresiones regulares para los tokens
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_ASIGNAR = r'='
t_PUNTOCOMA = r';'
t_MENORIGUAL = r'<='
t_PLUSPLUS = r'\+\+'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'
t_PUNTO = r'\.'
t_COMDOB = r'"'
t_DOSPUNTO = r':'
t_SUMA = r'\+'
t_MENOS = r'-'

# Definir tokens reservados
def t_RESERVADA(t):
    r'(for|int|System|println|program|read|printf|end)'
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z][a-zA-Z0-9\s]*'
    return t

def t_ENTERO(t):
    r'\d+'
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Función para realizar el análisis léxico
def realizar_analisis_lexico(code):
    lexer.input(code)
    tokens_lexico = []
    
    # Contadores de categorías de tokens
    counts = {
        'RESERVADA': 0,
        'IDENTIFICADOR': 0,
        'ENTERO': 0,
        'ASIGNAR': 0,
        'PUNTOCOMA': 0,
        'MENORIGUAL': 0,
        'PLUSPLUS': 0,
        'LLAIZQ': 0,
        'LLADER': 0,
        'PUNTO': 0,
        'COMDOB': 0,
        'DOSPUNTO': 0,
        'SUMA': 0,
        'MENOS' : 0
    }

    lexer.lineno = 1
    for tok in lexer:
        tokens_lexico.append({
            'type': tok.type,
            'value': tok.value,
            'line': tok.lineno,
        })
        if tok.type in counts:
            counts[tok.type] += 1

    return tokens_lexico, counts


# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASIGNAR COMDOB DOSPUNTO ENTERO IDENTIFICADOR LLADER LLAIZQ MENORIGUAL MENOS PARDER PARIZQ PLUSPLUS PUNTO PUNTOCOMA RESERVADA SUMA\n    expresion : RESERVADA PARIZQ RESERVADA IDENTIFICADOR ASIGNAR ENTERO PUNTOCOMA IDENTIFICADOR MENORIGUAL ENTERO PUNTOCOMA IDENTIFICADOR PLUSPLUS PARDER LLAIZQ RESERVADA PUNTO IDENTIFICADOR PUNTO RESERVADA PARIZQ COMDOB IDENTIFICADOR DOSPUNTO COMDOB SUMA IDENTIFICADOR PARDER PUNTOCOMA LLADER\n              | RESERVADA PUNTO IDENTIFICADOR PUNTO RESERVADA PARIZQ COMDOB IDENTIFICADOR DOSPUNTO COMDOB SUMA IDENTIFICADOR PARDER PUNTOCOMA \n              | LLAIZQ LLADER\n              | RESERVADA IDENTIFICADOR PARIZQ PARDER LLAIZQ RESERVADA IDENTIFICADOR IDENTIFICADOR IDENTIFICADOR PUNTOCOMA RESERVADA IDENTIFICADOR PUNTOCOMA RESERVADA IDENTIFICADOR PUNTOCOMA IDENTIFICADOR ASIGNAR IDENTIFICADOR SUMA IDENTIFICADOR PUNTOCOMA RESERVADA PARIZQ COMDOB IDENTIFICADOR COMDOB PARDER RESERVADA PUNTOCOMA LLADER \n    '
    
_lr_action_items = {'RESERVADA':([0,4,13,15,30,39,44,52,59,71,],[2,8,16,18,33,42,46,54,61,73,]),'LLAIZQ':([0,12,41,],[3,15,44,]),'$end':([1,7,43,74,76,],[0,-3,-2,-1,-4,]),'PARIZQ':([2,5,16,54,61,],[4,9,19,56,63,]),'PUNTO':([2,10,46,50,],[6,13,48,52,]),'IDENTIFICADOR':([2,6,8,18,20,21,22,24,32,33,34,42,47,48,51,55,58,65,66,],[5,10,11,21,23,24,25,27,35,36,37,45,49,50,53,57,60,67,68,]),'LLADER':([3,72,75,],[7,74,76,]),'PARDER':([9,37,38,68,69,],[12,40,41,70,71,]),'ASIGNAR':([11,49,],[14,51,]),'ENTERO':([14,26,],[17,29,]),'PUNTOCOMA':([17,27,29,36,40,45,57,70,73,],[20,30,32,39,43,47,59,72,75,]),'COMDOB':([19,28,56,62,63,67,],[22,31,58,64,65,69,]),'MENORIGUAL':([23,],[26,]),'DOSPUNTO':([25,60,],[28,62,]),'SUMA':([31,53,64,],[34,55,66,]),'PLUSPLUS':([35,],[38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expresion':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expresion","S'",1,None,None,None),
  ('expresion -> RESERVADA PARIZQ RESERVADA IDENTIFICADOR ASIGNAR ENTERO PUNTOCOMA IDENTIFICADOR MENORIGUAL ENTERO PUNTOCOMA IDENTIFICADOR PLUSPLUS PARDER LLAIZQ RESERVADA PUNTO IDENTIFICADOR PUNTO RESERVADA PARIZQ COMDOB IDENTIFICADOR DOSPUNTO COMDOB SUMA IDENTIFICADOR PARDER PUNTOCOMA LLADER','expresion',30,'p_expresion','analizador_sintactico.py',10),
  ('expresion -> RESERVADA PUNTO IDENTIFICADOR PUNTO RESERVADA PARIZQ COMDOB IDENTIFICADOR DOSPUNTO COMDOB SUMA IDENTIFICADOR PARDER PUNTOCOMA','expresion',14,'p_expresion','analizador_sintactico.py',11),
  ('expresion -> LLAIZQ LLADER','expresion',2,'p_expresion','analizador_sintactico.py',12),
  ('expresion -> RESERVADA IDENTIFICADOR PARIZQ PARDER LLAIZQ RESERVADA IDENTIFICADOR IDENTIFICADOR IDENTIFICADOR PUNTOCOMA RESERVADA IDENTIFICADOR PUNTOCOMA RESERVADA IDENTIFICADOR PUNTOCOMA IDENTIFICADOR ASIGNAR IDENTIFICADOR SUMA IDENTIFICADOR PUNTOCOMA RESERVADA PARIZQ COMDOB IDENTIFICADOR COMDOB PARDER RESERVADA PUNTOCOMA LLADER','expresion',31,'p_expresion','analizador_sintactico.py',13),
]

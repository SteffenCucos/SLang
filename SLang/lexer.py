import sys

import ply.lex as lex
from ply.lex import PlyLogger as Logger

class Lexer:
    '''
    A Lexer:
        Transforms a sequence of characters (input) into a sequence of tokens. 
        This process is called tokenization.
    '''
    tokens = [
        'INT',
        'FLOAT',
        'NAME',
        'PLUS',
        'MINUS',
        'DIVIDE',
        'MULTIPLY',
        'EQUALS'
    ]

    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_DIVIDE = r'\/'
    t_MULTIPLY = r'\*'
    t_EQUALS = r'\='
    t_ignore = r' '

    def t_FLOAT(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_INT(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_NAME(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = 'NAME'
        return t

    def t_error(self, t):
        print("Illegal characters!")
        t.lexer.skip(1)

    def __init__(self):
        logger = Logger(sys.stdout)
        self.lexer = lex.lex(debuglog=logger, errorlog=logger, module=self)

    def tokenize(self, input):
        self.lexer.input(input)
        while token := self.lexer.token():
            yield token
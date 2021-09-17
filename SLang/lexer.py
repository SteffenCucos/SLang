from typing import List
import inspect

from logger import Logger

import ply.lex
from ply.lex import LexToken as Token

def printCaller():
    print(inspect.stack()[1][3])

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
    ] # type : List[str]

    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_DIVIDE = r'\/'
    t_MULTIPLY = r'\*'
    t_EQUALS = r'\='
    t_ignore = r' '

    def t_FLOAT(self, t: Token) -> Token:
        r'\d+\.\d+'
        t.value = float(t.value)
        printCaller()
        return t

    def t_INT(self, t: Token) -> Token:
        r'\d+'
        t.value = int(t.value)
        printCaller()
        return t

    def t_NAME(self, t: Token) -> Token:
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = 'NAME'
        printCaller()
        return t

    def t_error(self, t: Token) -> Token:
        #print("Illegal characters!")
        printCaller()
        t.lexer.skip(1)

    def __init__(self, logger: Logger = None):
        self.logger = logger
        self.lexer = ply.lex.lex(debuglog=self.logger, errorlog=self.logger, module=self)

    def tokenize(self, input: str):
        self.logger.info("Tokenizing: '" + input + "'")
        self.lexer.input(input)
        while token := self.lexer.token():
            yield token
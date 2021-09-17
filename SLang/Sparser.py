from typing import List

from logger import Logger
from lexer import Lexer


import ply.yacc as yacc  # type: ignore
from ply.yacc import LRParser  # type: ignore


class Parser:
    '''
    A Parser
        Apply a grammar to a stream of tokens, generate an AST.
    '''

    def p_calc(self, p):
        '''
        calc : expression
             | empty
        '''
        print(p[1])

    def p_empty(self, p):
        '''
        empty : 
        '''
        p[0] = None

    def p_expression(self, p):
        '''
        expression : expression MULTIPLY expression
                   | expression DIVIDE expression 
                   | expression MINUS expression
                   | expression PLUS expression
        '''
        p[0] = (p[2], p[1], p[3])

    def p_expression_literal(self, p):
        '''
        expression : INT
                   | FLOAT
        '''
        p[0] = p[1]

    def __init__(self, lexer: Lexer = None, logger: Logger = None):
        self.logger = logger
        self.lexer = lexer
        self.tokens = lexer.tokens
        self.parser = yacc.yacc(debuglog=self.logger, errorlog=self.logger, module=self)

    def parse(self, input: str) -> None:
        return self.parser.parse(input)

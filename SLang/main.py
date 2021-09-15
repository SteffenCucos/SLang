from lexer import Lexer

def main():
    '''
    A compiler is made up of 3 parts
        A Lexer:
        A Parser
            Apply a grammar to the tokens, generate an AST.
        A Code generator
            Takes an AST and generates code to run.
    
    '''
    lexer = Lexer()
    for token in lexer.tokenize("1+2*3"):
        print(token)


if __name__ == "__main__":
    main()
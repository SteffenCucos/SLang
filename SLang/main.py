from lexer import Lexer

def main():
    '''

    A language to describe a vena model.
        Types:
            Model
            Dimension
            Member
        
        Talk to Rachel for ino day
        
        # Portable Customer Format
        # Fully describe a customers Models in a single format, including shared dimensions, shared members.

		Dim3 = Dimension 'Dim 3'
			Attribute 'A1'
			Member 'M' Attributes 'A1'

		SteffenCorp = Customer 'Steffen Corp Customer'
			 Model 'Model 1'
				 Dimension 'Dim 1'
					 Attribute 'A1'
					 Attribute 'A2'
					 Member 'M1'  Operator ~
					 Member 'M2'
						 Member 'M3','M3 Alias','',+
					 Member 'M4'  Alias 'M4 Alias'  Attributes 'A1,A2'  Operator -
				 Dimension 'Dim 2'
					...
				 Dim3
			 Model 'Model 2'
				 Dim3


    A compiler is made up of 3 parts
        A Lexer:
            Transforms a sequence of characters (input) into a sequence of tokens. 
            This process is called tokenization.
        A Parser
            Apply a grammar to the tokens, generate an AST.
        A Code generator
            Takes an AST and generates code to run.
    '''
    lexer = Lexer()
    for token in lexer.tokenize("abc = 1+2*3"):
        print(token)


if __name__ == "__main__":
    main()
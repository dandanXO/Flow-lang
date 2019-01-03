from tokens import TokenDataType, TokenList
from Lexer import Lexer


class Parser:
    def __init__(self, symbols):
        self.module = None
        self.prev_token = None
        self.state = None
        self.symbols = symbols
        
    def Parse(self, lexer):
        while not lexer.Ended():
            token = lexer.GetNextToken()

            print(token)

    def ParseVariable(self):
        pass
    


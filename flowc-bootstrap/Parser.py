from tokens import TokenDataType, TokenList
from Lexer import Lexer


class Parser:
    def __init__(self):
        self.module = None
        self.prev_token = None
        self.state = None
        
    def Parse(self, lexer):
        while not lexer.Ended():
            token = lexer.GetNextToken()

            print(token)

    def ruler(self):
        pass
        
    def GuessType(self, expr):
        #if type(expr) is
        pass 


from Constants.Tokens import TokenList
from Lexer import Lexer, Token


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


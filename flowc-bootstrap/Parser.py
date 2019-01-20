from Tokens import TokenDataType, TokenList
from Lexer import Lexer


class Parser:
    def __init__(self, lexer, env):
        self.lexer = lexer
        self.prev_token = None
        self.state = None
        self.env = env
        
    def Parse(self, lexer):
        while not lexer.Ended():
            token = lexer.GetNextToken()

            print(token)

    def ParseDeclaration(self):
        pass
    
    


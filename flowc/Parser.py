from Constants.Tokens import TokenList, TokenDataType
from Lexer import Lexer

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.prev_token = None
        self.declaration_table = {}
        
    def Parse(self):
        while not self.lexer.Ended():
            pass
    
    def MakeBinOp(self):
        pass
    

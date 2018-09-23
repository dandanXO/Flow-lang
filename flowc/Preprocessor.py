from enum import Enum

@unique
class PreprocessTokens:
    Bind = 1
    End = 2
    


class Preprocessor:
    def __init__(self, lexer):
        self.bindings = {}

        
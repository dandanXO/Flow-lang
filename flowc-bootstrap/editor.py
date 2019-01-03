EditorKeywords = [
    'bind',
    'if',
    'elif',
    'else',
    'end',
    'projPath',
    'pwd',
    'file',
    'path',
    'date',
    'year',
    'month',
    'day',
    'time',
    'hour12',
    'hour24',
    'minute',
    'second',
    'interprete',
    'compile',
    'graphic',
    'warn',
    'error',
    'msg',
    'line',
    'pos',
    'capture',
    'align'
]

EditorOperators = [
    '!',
    '!=',
    '%',
    '^',
    '&',
    '*',
    '(',
    ')',
    '-',
    '+',
    '=',
    '==',
    '|',
    '/',
    '<',
    '>',
    '<=',
    '>=',
    'or',
    'and',
    'not'
]

class Editor:
    def __init__(self, fp, symbols=[]):
        for symbol in symbols:
            if symbol in EditorKeywords:
                raise RuntimeError('[Editor] Found keyword inside input symbols!')
        self.symbolsTable = symbols
        self.file = fp

    def ProcessFile(self, temp_file):
        #Skipping comments
        pass

    def __del__(self):
        pass
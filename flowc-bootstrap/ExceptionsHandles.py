
def codeHighlight(line, start, end):
    highlights = ''
    for c in range(len(line)):
        if c < start or c > end:
            highlights += ' '
            continue
        highlights += '^'

class LexicalError(Exception):
    def __init__(self, msg, file_name, code, pos):
        self.msg = msg
        self.file_name = file_name
        self.pos = pos
        self.code = code

    def __str__(self):
        return '\nAt line {} inside {}:\n\t{}\n{}'\
        .format(self.pos[0], self.file_name, codeHighlight(self.code, self.pos[1], self.pos[2]), self.msg)

class SyntaxError(Exception):
    def __init__(self, msg):
        self.msg = msg

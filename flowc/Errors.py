
#TODO: implement syntax error
class SyntaxError(Exception):
    def __init__(self, msg, pos):
        self.msg = msg
        self.line = pos[0]
        self.col = pos[1]
    def __str__(self):
        return self.msg + ' @ ' + str(self.line) + ',' + str(self.col)

if __name__ == '__main__':
    import os
    raise SyntaxError('Syntax error raised', (2,3))

#coding=UTF-8
class SyntaxError(Exception):
    def __init__(self, msg, pos):
        self.msg = msg
        self.line = pos[0]
        self.col = pos[1]
    def __str__(self):
        return "{} @ line {} :{}".format(self.msg, str(self.line), str(self.col))

if __name__ == '__main__':
    raise SyntaxError('SyntaxError test', (0,0))


from ASTNode import ASTNode


class UnaryNode(ASTNode):
    def __init__(self, op, expression):
        super().__init__(self)
        self.op = op
        self.expr = expression
    
    def __str__(self):
        return 'UnaryNode({}, {})'.format(self.op, self.expr)

    def WalkThough(self):
        if not self.valid(self.expr):
            raise SyntaxError('[UnaryNode] Expression is not callable.')

        expr_ret = self.expr.WalkThough()

        if not(type(expr_ret) is int):
            raise SyntaxError('[UnaryNode] Expression is not an integer.')

        if self.op == '!':
            if expr_ret != 0:
                return 0
            return 1
        elif self.op == '-':
            return -expr_ret
        elif self.op == 'not':

        else:
            raise SyntaxError('[UnaryNode] Unknown operator.')


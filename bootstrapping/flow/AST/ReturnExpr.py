from AST import *

class ReturnExpression(ASTBase):
    def __init__(self, pos, expr=None):
        super().__init__('Return Expression', pos)
        self.expr = expr

    def __str__(self):
        return super().__str__() + "Expression => {}".format(self.expr)

    def GrowTree(self, module, builder, resources):
        if self.expr:
            builder.ret(self.expr.GrowTree(module, builder))
        else:
            builder.ret_void()
from AST import *

class FunctionCallExpression(ASTBase):
    def __init__(self, pos, func_ident):
        super().__init__("Function Call Expression Node", pos)
        self.func_ident = func_ident

    def __str__(self):
        return super().__str__() + "Function Identifier => {}".format(self.func_ident)

    def GrowTree(self, module, builder, resources):
        return super().GrowTree(module, builder)
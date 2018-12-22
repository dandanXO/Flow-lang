from AST import *

class VariableExpression(ASTBase):
    def __init__(self, ident, val_expr, pos):
        super().__init__("Variable Expression", pos)
        self.ident = ident
        self.val_expr = val_expr

    def __str__(self):
        return super().__str__() + "Identifier => {}\n\tValue Expression => {}".format(self.ident, self.val_expr)

    def GrowTree(self, module, builder, resources):
        # TODO: create variable lookup table
        return None
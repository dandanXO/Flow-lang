from AST import *

class ValueExpression(ASTBase):
    def __init__(self, pos, val, type, signed=True):
        super().__init__("Value Expression", pos)
        self.value = val
        self.type = type
        self.signed = signed

    def __str__(self):
        return super().__str__() + "Type => {}\n\tValue => {}\n\tSigned => {}".format(self.type, self.value, self.signed)

    def GrowTree(self, module, builder, resources):
        return ir.Constant(self.type, self.value)
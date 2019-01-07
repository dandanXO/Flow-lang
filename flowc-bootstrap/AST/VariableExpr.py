from AST import *

class VariableExpression(ASTBase):
    def __init__(self, pos, name, type, initializer=None):
        super().__init__("Variable Expression", pos)
        self.name = name
        self.type = type
        self.init_expr = initializer

    def __str__(self):
        return super().__str__() + "Name => {}\n\tVariable type => {}\n\tInitializer => {}"\
        .format(self.name, self.type, self.init_expr)

    def GrowTree(self, module, builder, resources):
        # TODO: create variable lookup table
        return None
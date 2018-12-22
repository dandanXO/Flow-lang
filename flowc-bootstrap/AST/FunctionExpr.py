from AST import *


class FunctionHeaderExpression(ASTBase):
    def __init__(self, pos, ident, parms, ret_type, varies):
        super().__init__("Function Header Expression Node", pos)
        self.ident = ident
        self.parms = parms
        self.parm_num = len(parms)
        self.varies = varies
        self.ret_type = ret_type

    def __str__(self):
        return super().__str__() + \
        "Identifier => {}\n\t\
        Varies => {}\n\t\
        Parameters => {}\n\t\
        Number of parameters => {}\n\t\
        Return type => {}\
        ".format(self.ident, self.varies, self.parms, self.parm_num, self.ret_type)

    def GrowTree(self, module, builder, resources):
        # TODO: NDY
        return ir.FunctionType(self.ret_type, self.parms)

class FunctionDeclaration(ASTBase):
    def __init__(self, pos, header, body):
        super().__init__("Function Declaration", pos)
        self.header = header
        self.body = body

    def __str__(self):
        return super().__str__() + "Header => {}\n\tBody => {}\
        ".format(self.header, self.body)

    def GrowTree(self, module, builder, resources):
        # Get function type from header
        funcType = self.header.GrowTree(module, builder)
        func = ir.Function(module, funcType, self.header.ident)
        self.body.GrowTree(func, builder)
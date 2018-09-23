from Constants.AST import BinaryOperation

class ExpressionBase:
    def __init__(self, name, line, col):
        self.name = name
        self.line = line
        self.col = col

    def codegen(self):
        return None

    def __str__(self):
        return "{} @ {}, {}".format(self.name, self.line, self.col)

class BinOpExpression(ExpressionBase):
    def __init__(self, op, expA, expB, pos):
        super.__init__('Binary Operation Expression', pos[0], pos[1])
        self.op = op
        self.expA = expA
        self.expB = expB

class BranchExpression(ExpressionBase):
    def __init__(self, condition, then_block, else_block, pos):
        super.__init__("Branch Expression", pos[0], pos[1])
        self.condit = condition
        self.then_block = then_block
        self.else_block = else_block

class FunctionProtoExpression(ExpressionBase):
    def __init__(self, ident, parms, body, ret_type, pos):
        super.__init__("Function Prototype Expression", pos[0], pos[1])
        self.ident = ident
        self.parms = parms
        self.parm_num = len(parms)
        self.body = body
        self.ret_type = ret_type
        
class ScopeExpression(ExpressionBase):
    def __init__(self, pos):
        super.__init__("Scope Expression", pos[0], pos[1])



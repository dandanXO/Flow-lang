from enum import Enum, unique
from llvmlite import ir
from Constants.Tokens import TokenList

@unique
class BinaryOperation(Enum):
    Addition = 1
    Subtract = 2
    Multiply = 3
    Divide = 4
    Remain = 5

    Not = 6
    Or = 7
    And = 8
    Xor = 9
    Shl = 10
    Shr = 11

@unique
class PrimitiveDataType(Enum):
    void = 0
    boolean = 1
    u8 = 2
    u16 = 3
    u32 = 4
    u64 = 5
    i8 = 6
    i16 = 7
    i32 = 8
    i64 = 9
    f32 = 10
    f64 = 11
    string = 12
    pointer = 13
    
@unique
class ValueType(Enum):
    null = 0
    number = 1
    pointer = 2
    string = 3
    boolean = 4
    tuple = 5
    array = 6

class ASTNodeBase:
    def __init__(self, name, pos):
        self.name = name
        self.line = pos[0]
        self.col = pos[1]
    def codegen(self, module, builder):
        return None
    def __str__(self):
        return "{} @ ({}, {})".format(self.name, self.line, self.col)

class ValueExpression(ASTNodeBase):
    def __init__(self, val, type, pos):
        super().__init__("Value Expression Node", pos)
        self.value = val
        self.type = type
    def __str__(self):
        return "{} @ ({}, {})\n\tType => {}\n\tValue => {}".format(self.name, self.line, self.col, self.type, self.value)
    def codegen(self, module, builder):
        return ir.Constant(self.type, self.value)

class VariableExpression(ASTNodeBase):
    def __init__(self, ident, val_expr, pos):
        super().__init__("Variable Expression Node", pos)
        self.ident = ident
    def __str__(self):
        return "{} @ ({}, {})\n\tIdentifier => {}".format(self.name, self.line, self.col, self.ident)
    def codegen(self, module, builder):
        # TODO: create variable lookup table
        return None

class BinOpExpression(ASTNodeBase):
    def __init__(self, op, lhs, rhs, pos):
        super().__init__("Binary Operation Expression Node", pos)
        self.op = op
        self.lhs = lhs
        self.rhs = rhs
    def __str__(self):
        return "{} @ ({}, {})\n\t   \
        Operator => {}\n\t  \
        LHS => {}\n\t   \
        RHS => {}\n\t   \
        ".format(self.name, self.line, self.col, self.op, self.lhs, self.rhs)
    def codegen(self, module, builder):
        # TODO: NDY
        lhs = self.lhs.codegen()
        rhs = self.rhs.codegen()

        if not(lhs) or not(rhs):
            return None
        # Integer
        if self.op == TokenList.kw_not:
            return None
        # Floating

        # Casting


class BranchExpression(ASTNodeBase):
    def __init__(self, condition, then_block, else_block, pos):
        super().__init__("Branch Expression Node", pos)
        self.condit = condition
        self.then_block = then_block
        self.else_block = else_block
    def __str__(self):
        return "{} @ ({}, {})\n\t   \
        Condition => {}\n\t  \
        Then => {}\n\t   \
        Else => {}\n\t   \
        ".format(self.name, self.line, self.col, self.condit, self.then_block, self.else_block)
    def codegen(self, module, builder):
        return super().codegen(module, builder)

class FunctionCallExpression(ASTNodeBase):
    def __init__(self, name, pos):
        super().__init__("Function Call Expression Node", pos)
        self.name = name
    def __str__(self):
        return "{} @ ({}, {})\n\tName => {}".format(self.name, self.line, self.col, self.name)
    def codegen(self, module, builder):
        return super().codegen(module, builder)

class FunctionHeaderExpression(ASTNodeBase):
    def __init__(self, ident, parms, ret_type, varies, pos):
        super().__init__("Function Header Expression Node", pos)
        self.ident = ident
        self.parms = parms
        self.parm_num = len(parms)
        self.varies = varies
        self.ret_type = ret_type
    def __str__(self):
        return "{} @ ({}, {})\n\t\t\
        Identifier => {}\n\t\t\
        Varies => {}\n\t\t\
        Parameters => {}\n\t\t\
        Number of parameters => {}\n\t\t\
        Return type => {}\
        ".format(self.name, self.line, self.col, self.ident, self.varies, self.parms, self.parm_num, self.ret_type)
    def codegen(self, module, builder):
        # TODO: NDY
        return ir.FunctionType(self.ret_type, self.parms)

class ScopeExpression(ASTNodeBase):
    def __init__(self, childs, ident, pos):
        super().__init__("Scope Expression Node", pos)
        self.childs = childs
        self.ident = ident
    def __str__(self):
        return "{} @ ({}, {})\n\t\t\tIdentifier => {}\n\t\t\tChilds => {}\
        ".format(self.name, self.line, self.col, self.ident, self.childs)
    def codegen(self, module, builder):
        #TODO: NDY
        block = module.append_basic_block(self.ident)
        builder = ir.IRBuilder(block)
        if self.childs:
            for child in self.childs:
                child.codegen(module, builder)

class FunctionDeclaration(ASTNodeBase):
    def __init__(self, header, body, pos):
        super().__init__("Function Declaration Node", pos)
        self.header = header
        self.body = body
    def __str__(self):
        return "{} @ ({}, {})\n\tHeader => {}\n\tBody => {}\
        ".format(self.name, self.line, self.col, self.header, self.body)
    def codegen(self, module, builder):
        # Get function type from header
        funcType = self.header.codegen(module, builder)
        func = ir.Function(module, funcType, self.header.ident)
        self.body.codegen(func, builder)
    
class ReturnExpression(ASTNodeBase):
    def __init__(self, expr=None):
        self.expr = expr
    def __str__(self):
        return "{} @ ({}, {})\n\tExpression => {}".format(self.name, self.line, self.col, self.expr)
    def codegen(self, module, builder):
        if self.expr:
            builder.ret(self.expr.codegen(builder))
        else:
            builder.ret_void()

if __name__ == '__main__':
    mod = ir.Module(name=__file__)
    fh = FunctionHeaderExpression('main', [], ir.VoidType(), False, (0,0))
    fe = FunctionDeclaration(fh, ScopeExpression(None, 'AAA', [0,0]), (0,0))
    print(fe)
    fe.codegen(mod, None)
    
    fh2 = FunctionHeaderExpression('second_func', [], ir.VoidType(), False, (0,0))
    fe2 = FunctionDeclaration(fh2, ScopeExpression(None, 'BBB', [0,0]), (0,0))
    print(fe2)
    fe2.codegen(mod, None)

    print(mod.functions)

    print(mod)


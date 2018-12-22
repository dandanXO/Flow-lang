from AST import *


class BinOpExpression(ASTBase):
    def __init__(self, pos, op, expA, expB):
        super().__init__("Binary Operation Expression", pos)
        self.op = op
        self.expA = expA
        self.expB = expB

    def __str__(self):
        return super().__str__() + \
        "Operator => {}\n\t\
        ExpressionA => {}\n\t\
        ExpressionB => {}\
        ".format(self.op, self.expA, self.expB)

    def GrowTree(self, module, builder, resources):
        # TODO: NDY
        lhs = self.expA.GrowTree(module, builder)
        rhs = self.expB.GrowTree(module, builder)

        if not(lhs) or not(rhs):
            return None

        # Condition related
        if self.op == TokenList.kw_not:
            return builder.not_(lhs)
        if self.op == TokenList.kw_or:
            return builder.or_(lhs, rhs)
        if self.op == TokenList.kw_and:
            return builder.and_(lhs, rhs)
        if self.op == TokenList.kw_xor:
            return builder.xor(lhs, rhs)
            
        # Comparison
        cmpop = ''
        if self.op == TokenList.sym_equal:
            cmpop = '=='
        if self.op == TokenList.sym_not_equal:
            cmpop = '!='
        if self.op == TokenList.sym_greater:
            cmpop = '>'
        if self.op == TokenList.sym_greater_equal:
            cmpop = '>='
        if self.op == TokenList.sym_less:
            cmpop = '<'
        if self.op == TokenList.sym_less_equal:
            cmpop = '<='

        # Maths
        if self.op == TokenList.sym_add:
            cmpop = '+'
        if self.op == TokenList.sym_minus:
            cmpop = '-'
        if self.op == TokenList.sym_asterisk:
            cmpop = '*'
        if self.op == TokenList.sym_divide:
            cmpop = '/'
        if self.op == TokenList.sym_shift_left:
            cmpop = '<<'
        if self.op == TokenList.sym_shift_right:
            cmpop = '>>'
        if self.op == TokenList.sym_remainder:
            cmpop = '%'
        
        return None
from ASTNode import ASTNode
from Tokens import TokenOperators as ops
from Tokens import TokenReserveds as reserved

class BinOpNode(ASTNode):
    def __init__(self, lhs, op, rhs):
        super().__init__(self)
        self.op = op
        self.lhs = lhs
        self.rhs = rhs
    
    def __str__(self):
        return 'BinOpNode({}, {}, {})'.format(self.lhs, self.op, self.rhs)
    
    def WalkThough(self):
        # make sure lhs and rhs both has WalkThough
        if not self.valid(self.lhs):
            raise SyntaxError('[BinOpNode] Left-hand side is not callable.')

        lhs_ret = self.lhs.WalkThough()
        
        if self.valid(self.rhs):
            raise SyntaxError('[BinOpNode] Right-hand side is not callable.')
            
        rhs_ret = self.rhs.WalkThough()

        if not(type(lhs_ret) is int):
                raise SyntaxError('[BinOpNode] Left-hand side is not an integer.')
        if not(type(rhs_ret) is int):
            raise SyntaxError('[BinOpNode] Right-hand side is not an integer.')

        # integer operators
        if self.op == ops['%']:
            # remainder
            return lhs_ret % rhs_ret

        elif self.op == ops['^']:
            # xor
            return lhs_ret ^ rhs_ret

        elif self.op == ops['&']:
            # and
            return lhs_ret & rhs_ret

        elif self.op == ops['*']:
            # multiply
            return lhs_ret * rhs_ret

        elif self.op == ops['-']:
            # minus
            return lhs_ret - rhs_ret

        elif self.op == ops['+']:
            # add
            return lhs_ret + rhs_ret

        elif self.op == ops['|']:
            # or
            return lhs_ret | rhs_ret

        elif self.op == ops['/']:
            # divide
            if rhs_ret == 0:
                raise ValueError('[BinOpNode] Cannot divide by zero.')
            
            return lhs_ret / rhs_ret

        elif self.op == ops['<<']:
            # shift left
            return lhs_ret << rhs_ret

        elif self.op == ops['>>']:
            # shift right
            return lhs_ret >> rhs_ret

        # comparations
        elif self.op == ops['==']:
            if lhs_ret == rhs_ret:
                return 1
            return 0

        elif self.op == ops['!=']:
            if lhs_ret != rhs_ret:
                return 1
            return 0

        elif self.op == ops['<']:
            if lhs_ret < rhs_ret:
                return 1
            return 0

        elif self.op == ops['<=']:
            if lhs_ret <= rhs_ret:
                return 1
            return 0

        elif self.op == ops['>']:
            if lhs_ret > rhs_ret:
                return 1
            return 0

        elif self.op == ops['>=']:
            if lhs_ret >= rhs_ret:
                return 1
            return 0

        # condition operators
        elif self.op == reserved['or']:
            if lhs_ret != 0 or rhs_ret != 0:
                return 1
            return 0

        elif self.op == reserved['xor']:
            if lhs_ret != rhs_ret:
                return 1
            return 0

        elif self.op == reserved['and']:
            if lhs_ret != 0 and rhs_ret != 0:
                return 1
            return 0

        else:
            raise SyntaxError('[BinOpNode] Unknown operator.')
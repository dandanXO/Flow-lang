from ASTNode import ASTNode

class IfBranchNode(ASTNode):
    def __init__(self, condition, true_block, false_block=None):
        super().__init__(self)
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

    def __str__(self):
        return 'IfBranchNode({}, {}, {})'\
            .format(self.condition, self.true_block, self.false_block)

    def WalkThough(self):
        if self.valid(self.condition):
            condit = self.condition.WalkThough()
        else:
            raise SyntaxError('[IfBranchNode] Condition is not callable.')

        # if it is not a boolean or integer
        if not(type(condit) is int):
            raise ValueError('[IfBranchNode] Invalid condition.')

        if condit != 0:
            if self.valid(self.true_block):
                return self.true_block.WalkThough()
            else:
                raise SyntaxError('[IfBranchNode] True expression is not callable.')
        else:
            # has false situation
            if self.false_block:
                if self.valid(self.false_block):
                    return self.false_block.WalkThough()
                else:
                    raise SyntaxError('[IfBranchNode] False expression is not callable.')
            return


        
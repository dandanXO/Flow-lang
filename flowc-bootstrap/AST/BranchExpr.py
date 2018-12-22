from AST import *

class BranchExpression(ASTBase):
    def __init__(self, pos, condition, then_block, else_block):
        super().__init__("Branch Expression", pos)
        self.condit = condition
        self.then_block = then_block
        self.else_block = else_block

    def __str__(self):
        return super().__str__() + \
        "Condition => {}\n\t\
        Then => {}\n\t\
        Else => {}\
        ".format(self.condit, self.then_block, self.else_block)
         
    def GrowTree(self, module, builder, resources):
        condition = self.condit.GrowTree(module, builder)
        if condition == None:
            raise RuntimeError('No condition AST found. {}'.format(self))
        
        if self.else_block:
            with builder.if_else(condition) as (if_true, if_false):
                with if_true:
                    return self.then_block.GrowTree(module, builder)
                with if_false:
                    return self.else_block.GrowTree(module, builder)

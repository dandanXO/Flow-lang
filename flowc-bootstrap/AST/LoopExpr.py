from AST import *

class LoopExpression(ASTBase):
    def __init__(self, pos, condition, loop_body, check_first=True):
        super().__init__('Loop Expression', pos)
        self.check_first = check_first
        self.condition = condition
        self.loop_body = loop_body
    
    def __str__(self):
        return super().__str__() + "Condition => {}\n\tCheck before loop => {}\n\tBody => {}"\
        .format(self.condition, self.check_first, self.loop_body)

    def GrowTree(self, module, builder, resources):
        initial_block = builder.append_basic_block('loop.init')
        check_block = builder.append_basic_block('loop.check')
        body_block = builder.append_basic_block('loop.body')

        builder.position_at_end(initial_block)
        if self.check_first:
            # check condition before get into loop body
            builder.branch(check_block)
        else:
            #go into loop body first
            builder.branch(body_block)


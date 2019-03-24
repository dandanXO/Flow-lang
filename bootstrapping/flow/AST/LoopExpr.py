from AST import *

class LoopExpression(ASTBase):
    def __init__(self, pos, condition, loop_body, check_first=True, infinity_loop=True):
        super().__init__('Loop Expression', pos)
        self.check_first = check_first
        self.condition = condition
        self.loop_body = loop_body
        self.infinity_loop = infinity_loop
    
    def __str__(self):
        return super().__str__() + "Condition => {}\n\tCheck before loop => {}\n\tBody => {}"\
        .format(self.condition, self.check_first, self.loop_body)

    def GrowTree(self, module, builder, resources):
        check_block = builder.append_basic_block('loop.check')
        body_block = builder.append_basic_block('loop.body')

        with builder.goto_block(check_block):
            pass

        with builder.goto_block(body_block):
            pass

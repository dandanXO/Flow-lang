from AST import *

class ScopeExpression(ASTBase):
    def __init__(self, pos, child, ident):
        super().__init__("Scope Expression", pos)
        self.childs = child
        self.ident = ident

    def __str__(self):
        return "{} @ ({}, {})\n\t\t\tIdentifier => {}\n\t\t\tChild => {}\
        ".format(self.name, self.line, self.col, self.ident, self.childs)

    def GrowTree(self, module, builder, resources):
        #TODO: NDY
        block = module.append_basic_block(self.ident)
        builder = ir.IRBuilder(block)
        if self.childs:
            for child in self.childs:
                child.GrowTree(module, builder)
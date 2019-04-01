from ASTNode import ASTNode

class VarDeclNode(ASTNode):
    def __init__(self, identifier, vtype, value, mutable=True):
        self.indent = identifier
        self.type = vtype
        self.value = value
        self.mutable = mutable

    def __str__(self):
        return 'VarDeclNode({}, {}, {}, {})'.format(self.indent, self.type, self.value, self.mutable)

    def WalkThough(self):
        pass
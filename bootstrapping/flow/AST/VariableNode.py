from ASTNode import ASTNode

class VariableDeclareNode(ASTNode):
    def __init__(self, identifier, vtype, value, mutable=True):
        self.indent = identifier
        self.type = vtype
        self.value = value
        self.mutable = mutable
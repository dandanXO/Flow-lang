from ASTNode import ASTNode

class FunctionHeaderNode(ASTNode):
    def __init__(self, name, args_type=[], return_type=None, varies=False):
        super().__init__(self)
        self.name = name
        self.args_type = args_type
        self.return_type = return_type
        self.varies = varies

    def __str__(self):
        return 'FunctionHeaderNode({}, {}, {}, {})'\
            .format(self.name, self.args_type, self.return_type, self.varies)

class FunctionNode(ASTNode):
    def __init__(self, header, body):
        super().__init__(self)
        self.header = header
        self.body = body

class FunctionCall(ASTNode):
    def __init__(self, name, args):
        super().__init__(self)
        self.name = name
        self.arguments = args
    
    def __str__(self):
        return 'FunctionCall({}, {})'.format(self.name, self.arguments)
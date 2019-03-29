
class ASTNode:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Empty {} node'.format(self.name)

    def CodeGen(self):
        raise NotImplementedError('Function \'CodeGen\' inside {} was not implemented!')
    
    def WalkThough(self):
        raise NotImplementedError('Function \'WalkThough\' inside {} was not implemented!')

    def valid(self, member):
        # make sure lhs and rhs both has WalkThough
        if not hasattr(member, 'WalkThough'):
            return False
        return True
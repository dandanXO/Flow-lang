from os import path
class CompileUnit:
    def __init__(self, in_file, config):
        self.file_name = in_file
        self.full_path = path.abspath(in_file)
        self.config = config

    #return (status, output)
    def compile(self):
        pass
    
    

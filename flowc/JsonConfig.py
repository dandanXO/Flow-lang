import json

class JsonConfig:
    def __init__(self, file_path):
        try:
            self.config_file = open(file_path, 'r+', encoding='UTF-8').read()
        except FileNotFoundError:
            print('Configure file not found')
            f = open(file_path, 'w+', encoding='UTF-8')
            f.close()
            self.config_file = open(file_path, 'r+', encoding='UTF-8').read()
        
        if len(self.config_file) == 0:
            raise RuntimeError('Empty configure file: {}'.format(file_path))
        self.config = json.loads(self.config_file)
        print(self.config)
    def initialize(self):
        pass
if __name__ == '__main__':
    jc = JsonConfig('project.json')
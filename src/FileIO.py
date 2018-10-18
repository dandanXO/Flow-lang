import os

def ReadFileByte(file_path, n=-1):
    file = open(file_path, 'rb')
    buff = file.read(n)
    file.close()
    return buff

def ReadFileText(file_path, n=-1):
    file = open(file_path, 'r', encoding='utf-8')
    buff = file.read(n)
    file.close()
    return buff

def GetFileSize(file):
    return os.path.getsize(file)

if __name__ == '__main__':
    print('FileIO test')
    print('Test file: ', __file__)
    print('[ReadFileByte] Byte read: ', len(ReadFileByte(__file__)))
    print('[ReadFileText], Character read: ', len(ReadFileText(__file__)))
    print('[GetFileSize] Size of test file: ', GetFileSize(__file__))
from argparse import ArgumentParser, FileType
from Defaults import DEFAULT_PROJECT_ROOT, DEFAULT_PROJECT_FILE

VERSION = 'v0'

if __name__ == '__main__':
    ap = ArgumentParser(description='Flow Language Compiler ' + VERSION)
    #optional
    ap.add_argument('files', nargs='*', help='Source code files', type=FileType('r'))
    ap.add_argument('-emit-llvm', help='Output LLVM IR code', action='store_true')
    ap.add_argument('-emit-processed', help='Output preprocessed code', action='store_true')
    args = vars(ap.parse_args())
    print(args)
    #if no file given
    if len(args['files']) == 0:
        print('No input files.')
        ap.print_help()
        exit()
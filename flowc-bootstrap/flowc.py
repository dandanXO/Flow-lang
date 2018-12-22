from argparse import ArgumentParser
from paths import DEFAULT_PROJECT_ROOT, DEFAULT_PROJECT_FILE


if __name__ == '__main__':
    ap = ArgumentParser(description='Flow Programming Language Compiler')
    #actions
    ap.add_argument('action', choices=['create', 'build', 'clean'])
    ap.add_argument('-root', help='Redirect PROJECT_ROOT to target directory', default=DEFAULT_PROJECT_ROOT)
    ap.add_argument('-proj', help='Redirect CONFIG_FILE to target path', default=DEFAULT_PROJECT_FILE)
    args = ap.parse_args()

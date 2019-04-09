from lark import Lark

with open('grammar.lark', 'r') as f:
            GRAMMAR = f.read()

if __name__ == '__main__':
    parser = Lark(grammar=GRAMMAR, start='statement')

    test_code = """
    if a == 1 {
        #
    }elif a {

    }elif b {

    }


    """

    print(parser.parse(test_code).pretty())
    ast = parser.parse
    while True:
        try:
            uin = input('~> ')
        except EOFError:
            break
        print(ast(uin))
    
# Workflow
# get raw syntax tree
# convert to AST with error detection
# return AST


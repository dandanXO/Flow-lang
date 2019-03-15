from Tokens import TokenList, TokenReserveds, TokenTypes
import ply.lex as plex
import re

# plex will use this
tokens = TokenList
reserved_words = TokenReserveds + TokenTypes

# Regex
hex_checker = re.compile(r'0x[^\s]([0-9a-f]*|[0-9A-F]*)')
binary_checker = re.compile(r'([10]+)b')


# Ignore comment
t_ignore_COMMENT = r'#.*'

# String
t_STR_LITERAL= r'\"([^\\\n]|(\\.))*?\"'

# Identifier
def t_IDENTIFIER(t):
    r"[_a-zA-Z][\w]*"
    #change type if it is a reserved word
    t.type = reserved_words.get(t.type, d="IDENTIFIER")
    return t

# Float literal
def t_FLOAT_LITERAL(t):
    r'(?:\d+)?\.(\d+)'
    #convert string into float number
    try:
        t.value = float(t.value)
        return t
    except ValueError:
        pass

#Binary numbers, heximal numbers and decimal numbers
def t_INT_LITERAL(t):
    r'(([10]+)b)|(^0x([0-9a-f]+|[0-9A-F]+))|([0-9]+)'

    if binary_checker.match(t.value):
        #it is a binary number
        try:
            #chop out the 'b' and attempt to convert it into a decimal number
            t.value = int(t.value[:-1], 2) 
            return t
        except ValueError:
            pass
    elif hex_checker.match(t.value):
        #heximal number
        try:
            t.value = int(t.value, 16)
            return t
        except ValueError:
            pass
    else:
        #decimal number
        # we won't accept numbers that start with zero
        if len(t.value) > 1 and t.value[0] == '0':
            pass
        else:
            try:
                t.value = int(t.value)
                return t
            except ValueError:
                pass
                
def t_error(t):
    print('Unknown token found!\n Text: {}'.format(t.value))
    exit(-1)

# Unit test
if __name__ == '__main__':
    print('Unit Test: Lexer')
    #create lexer
    lex = plex.lex()

from Tokens import TokenList, TokenReserveds, TokenOperators
import ply.lex as plex
import re

class Lexer:
    # plex will use this
    tokens = TokenList
    
    def __init__(self, text):
        self.text = text
        # Regex
        self.hex_checker = re.compile(r'0x[^\s]([0-9a-f]*|[0-9A-F]*)')
        self.binary_checker = re.compile(r'([10]+)b')
    
    def __iter__(self):
        return self.lex.__iter__()
    
    def __next__(self):
        return next(self.lex)

    def build(self, **args):
        self.lex = plex.lex(object=self, **args)
        self.lex.input(self.text)
        self.lex.lineno = 1

############################################
#           LEXER DEFINATIONS        
############################################
    #Ignore space and tabs
    t_ignore = ' \t' 
        
    # Capture string
    t_STR_LITERAL= r'\"([^\\\n]|(\\.))*?\"'

    # Capture character
    t_CHAR_LITERAL = r'\'\w{0,1}\''
    
    #register symbols
    t_SYM_NOT = r'\!'
    t_SYM_NOT_EQUAL = r'\!\='
    t_SYM_AT = r'\@'
    t_SYM_COLON = r'\:'
    t_SYM_DOLLAR = r'\$'
    t_SYM_REMAINDER = r'\%'
    t_SYM_ASSIGN_REMAINDER = r'\%\='
    t_SYM_XOR = r'\^'
    t_SYM_ASSIGN_XOR = r'\^\='
    t_SYM_AND = r'\&'
    t_SYM_ASSIGN_AND = r'\&\='
    t_SYM_ASTERISK = r'\*'
    t_SYM_ASSIGN_MULTIPLY = r'\*\='
    t_SYM_PAREN_OPEN = r'\('
    t_SYM_PAREN_CLOSE = r'\)'
    t_SYM_MINUS = r'\-'
    t_SYM_MINUS_ONE = r'\-\-'
    t_SYM_ASSIGN_SUBTRACT = r'\-\='
    t_SYM_ADD = r'\+'
    t_SYM_PLUS_ONE = r'\+\+'
    t_SYM_ASSIGN_PLUS = r'\+\='
    t_SYM_ASSIGN = r'\='
    t_SYM_EQUAL = r'\=\='
    t_SYM_BRACE_OPEN = r'\['
    t_SYM_BRACE_CLOSE = r'\]'
    t_SYM_BRACKET_OPEN = r'\{'
    t_SYM_BRACKET_CLOSE = r'\}'
    t_SYM_OR = r'\|'
    t_SYM_ASSIGN_OR = r'\|\='
    t_SYM_DIVIDE = r'\/'
    t_SYM_ASSIGN_DIVIDE = r'\/\='
    t_SYM_SEMICOLON = r'\;'
    t_SYM_LESS = r'\<'
    t_SYM_LESS_EQUAL = r'\<\='
    t_SYM_SHIFT_LEFT = r'\<\<'
    t_SYM_ASSIGN_SHIFT_LEFT = r'\<\<\='
    t_SYM_GREATER = r'\>'
    t_SYM_GREATER_EQUAL = r'\>\='
    t_SYM_SHIFT_RIGHT = r'\>\>'
    t_SYM_ASSIGN_SHIFT_RIGHT = r'\>\>\='
    t_SYM_COMMA = r'\,'
    t_SYM_RANGE = r'\~'
    
    # treat comment as newline
    def t_ignore_COMMENT(self, t):
        r'\#.*'

    #counting newline
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Identifier
    def t_IDENTIFIER(self, t):
        r"[_a-zA-Z][\w]*"
        #change type if it is a reserved word
        t.type = TokenReserveds.get(t.value, "IDENTIFIER")
        return t

    # Float literal
    def t_FLOAT_LITERAL(self, t):
        r'(?:\d+)?\.(\d+)'
        #convert string into float number
        try:
            t.value = float(t.value)
            return t
        except ValueError:
            pass

    #Binary numbers, heximal numbers and decimal numbers
    def t_INT_LITERAL(self, t):
        r'(([10]+)b)|(^0x([0-9a-f]+|[0-9A-F]+))|([0-9]+)'

        if self.binary_checker.match(t.value):
            #it is a binary number
            try:
                #chop out the 'b' and attempt to convert it into a decimal number
                t.value = int(t.value[:-1], 2) 
                return t
            except ValueError:
                pass
        elif self.hex_checker.match(t.value):
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
    
    def t_error(self, t):
        illegal_checker = re.compile(r'\'\w{2,}\'')
        single_quote_checker = re.compile(r'\'.*$[^\']')
        error_msg = 'Undefined token found!'
        if illegal_checker.match(t.value):
            error_msg = 'Character literal should not contain more than one characters!'
        elif single_quote_checker.match(t.value):
            error_msg = 'Quote did not paired!'
        
        #print out error message
        print('\nError: {}\n\n```\n\n{}\n\n```\nin line {} at position {}'.
            format(error_msg, t.value[:t.value.find('\n')], t.lineno, self.cal_column(t)))
        exit(-1)

    def cal_column(self, tok):
        line_start = self.text.rfind('\n', 0, tok.lexpos) + 1
        return (tok.lexpos - line_start) + 0

    def print_token(self, t):
        print('Token {} ({}) in line {} at pos {}'.format(t.type, t.value, t.lineno, self.cal_column(t)))

# Unit test
if __name__ == '__main__':
    print('Unit Test: Lexer')
    with open('testcode/lexer.text.flo', 'r') as f:
        test_code = f.read()

    #create lexer
    lexer = Lexer(test_code)
    lexer.build()

    for tok in lexer:
        lexer.print_token(tok)

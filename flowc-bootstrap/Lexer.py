from Tokens import TokenList, TokenReserveds, TokenOperators, TokenShapeless, TokenReserveds
import ply.lex as plex
import re


class LexicalError(Exception):
    def __init__(self, reason, details):
        self.reason = reason
        self.details = details

    def __str__(self):
        return '\n{}\nLexical Error: {}\nCompilation terminated.'.format(self.details, self.reason)

# The lexer class
class Lexer:
    # plex will use this
    tokens = TokenList
    
    def __init__(self, text, **args):
        self.text = text
        # Regex
        self.hex_checker = re.compile(r'0x[^\s]([0-9a-f]*|[0-9A-F]*)')
        self.binary_checker = re.compile(r'([10]+)b')
        self.single_quote_checker = re.compile(r'\'\".*$[^\'\"]')
        self.illegal_character_checker = re.compile(r'\'\w{2,}\'')

        self.lex = plex.lex(object=self, **args)
        self.lex.input(self.text)
        self.lex.lineno = 1

    #change input
    def input(self, text):
        self.text = text
        self.lex.input(text)
    
    #bridge of self.lex.token
    def token(self):
        return self.lex.token()
    
    def __iter__(self):
        return self.lex.__iter__()
    
    def __next__(self):
        return next(self.lex)

############################################
#           LEXER DEFINATIONS        
############################################

    #Ignore spaces and tabs
    t_ignore = ' \t'
    # treat comment as newline
    def t_ignore_COMMENT(self, t):
        r'\#.*'
        
    # Capture string
    def t_STR_LITERAL(self, t):
        r'\"([^\\\n]|(\\.))*?\"'
        t.value = t.value[1:-1]
        return t

    # Capture character
    def t_CHAR_LITERAL(self, t):
        r'\'([^\\\n]|(\\.))*?\''
        t.value = t.value[1:-1]
        return t

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

    #Counting newline
    def t_newline(self, t):
        r'\n+'
        #tracking line number
        t.lexer.lineno += len(t.value)

    # Capture identifiers (Only english letters and underscores!)
    def t_IDENTIFIER(self, t):
        r"[_a-zA-Z][\w]*"
        #recognize reserved words
        t.type = TokenReserveds.get(t.value, "IDENTIFIER")
        return t

    # Capture float literal
    def t_FLOAT_LITERAL(self, t):
        r'(?:\d+)?\.(\d+)'
        #convert string into float number
        try:
            t.value = float(t.value)
            return t
        except ValueError:
            pass

    # Capture binary numbers, heximal numbers and decimal numbers
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
            #it is a heximal number
            try:
                t.value = int(t.value, 16)
                return t
            except ValueError:
                pass
        else:
            #it is a decimal number
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

        #try to analysis reason
        reason = self.analysis_reason(t)
        #extract the line where error occur
        error_content = t.lexer.lexdata.split('\n')[t.lineno-1]
        
        error_text = t.value[:t.value.find('\n')]
        error_pos = error_content.find(error_text)

        underline = [' '] * len(error_content)
        for i in range(len(error_text)):
            underline[error_pos+i] = '^'
        underline = ''.join(underline)

        detail_msg = 'In line {} :\n```\n\n{}\n{}\n\n```'.format(t.lineno, error_content, underline)
        #submit the error
        try:
            raise LexicalError(reason, detail_msg)
        except LexicalError as e:
            print(e)
            exit(-1)

    def analysis_reason(self, t):

        if self.single_quote_checker.match(t.value):
            return 'Quote did not paired!'
        elif self.illegal_character_checker.match(t.value):
            return 'Character literal should not contain more than one characters!'
        else:
            return 'Illegal character(s) found!'

    def cal_column(self, tok):
        line_start = self.text.rfind('\n', 0, tok.lexpos) + 1
        return (tok.lexpos - line_start) + 0

    def print_token(self, t):
        print('Token {} ({}) in line {} at pos {}'.format(t.type, t.value, t.lineno, self.cal_column(t)))

def UnitTest():
    print('Unit Testing: Lexer\n')

    #create lexer
    lexer = Lexer('')
    
    # Comment
    print('* Comment --- ', end='')
    lexer.input('# Test comment here 註釋在這裡')
    assert lexer.token() == None, 'Failed!'
    print('Pass')

    # Identifier
    print('* Identifier --- ', end='')
    lexer.input('id')
    tok = lexer.token()
    assert tok.type == 'IDENTIFIER' and tok.value == 'id', 'Failed!'
    print('Pass')

    # Reserved word
    print('* Reserved words --- ', end='')
    for rw in list(TokenReserveds.keys()):
        lexer.input(rw)
        assert lexer.token().type == TokenReserveds[rw], '{} test failed!'.format(rw)
    print('Pass')

    # Operators
    print('* Operators ---', end='')
    for op in list(TokenOperators.keys()):
        lexer.input(op)
        assert lexer.token().type == TokenOperators[op], '{} test failed!'.format(op)
    print('Pass')
    
    # Character
    print('* Character --- ', end='')
    test_char = ['0','1','2','3','4','5','6','7','8','9',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','~','!','@','#','$','%','^','&','*','(',')','_','+','-','=','{','[','}',']','|',':',';','\\\"','\\\'','<',',','>','.','?','/']
    for ch in test_char:
        lexer.input('\'{}\''.format(ch))
        tok = lexer.token()
        assert tok.type == 'CHAR_LITERAL' and tok.value == '{}'.format(ch), '\'{}\' test failed!'.format(ch)
    print('Pass')

    # Character with special character
    print('* Special character --- ', end='')
    test_str = ['\\n', '\\t', "\\\'", '\\\"']
    for ch in test_str:
        lexer.input('\'{}\''.format(ch))
        tok = lexer.token()
        assert tok.type == 'CHAR_LITERAL' and tok.value == '{}'.format(ch), '\'{}\' test failed!'.format(ch)
    print('Pass')

    # Empty character
    print('* Empty character --- ', end='')
    lexer.input('\'\'')
    tok = lexer.token()
    assert tok.type == 'CHAR_LITERAL' and tok.value == '', 'Failed!'
    print('Pass')

    # String
    print('* String --- ', end='')
    lexer.input('\" 0123456789 abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+-={[}]|:;\\\"\\\'<,>.?/\"')
    tok = lexer.token()
    assert tok.type == 'STR_LITERAL', 'Failed!'
    print('Pass')

    print('* Empty string --- ', end='')
    lexer.input('\"\"')
    tok = lexer.token()
    assert tok.type == 'STR_LITERAL' and tok.value == '', 'Failed!'
    print('Pass')
    
    # Float
    print('* Float --- ', end='')
    lexer.input('0.123')
    tok = lexer.token()
    assert tok.type == 'FLOAT_LITERAL' and tok.value == 0.123, 'Failed!'
    print('Pass')

    return True

# Unit Testing
if __name__ == '__main__':
    UnitTest()
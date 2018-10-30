from Constants.Tokens import TokenList
import re
from Errors import SyntaxError
from enum import Enum, unique

dec_pattern = r'^(0|[^\s0.])\d+$' 
float_pattern = r'^([0-9]*)\.[0-9]+$' 
hex_pattern = r'^0x[0-9a-fA-F]+$'
bin_pattern = r'\b([10]+)b\b'

@unique
class TokenDataType(Enum):
    none = 0
    integer = 1
    floating = 2
    string = 3

class Token:
    def __init__(self, id, pos, kind=TokenDataType.none, data=None):
        self.id = id
        self.pos = pos
        self.kind = kind
        self.data = data
    
    def __str__(self):
        data_msg = ""
        if self.kind != TokenDataType.none:
            data_msg = ' with data "' + str(self.data) + '"'
        return 'Token ' + self.id.value + data_msg + ' at ' + str(self.pos) + ''

class Lexer:
    def __init__(self, code=None):
        self.code = code
        self.cursor = 0
        self.line = 1
        self.col = 1

        self.lookup = {}
        #Keywords
        self.lookup['nil'] = TokenList.kw_nil
        self.lookup['for'] = TokenList.kw_for
        self.lookup['in'] = TokenList.kw_in
        self.lookup['continue'] = TokenList.kw_continue
        self.lookup['break'] = TokenList.kw_break
        self.lookup['if'] = TokenList.kw_if
        self.lookup['else'] = TokenList.kw_else
        self.lookup['not'] = TokenList.kw_not
        self.lookup['or'] = TokenList.kw_or
        self.lookup['xor'] = TokenList.kw_xor
        self.lookup['and'] = TokenList.kw_and
        self.lookup['true'] = TokenList.kw_true
        self.lookup['false'] = TokenList.kw_false
        self.lookup['while'] = TokenList.kw_while
        self.lookup['return'] = TokenList.kw_return
        #Primitive types
        self.lookup['let'] = TokenList.pt_let
        self.lookup['bool'] = TokenList.pt_bool
        self.lookup['u8'] = TokenList.pt_u8
        self.lookup['u16'] = TokenList.pt_u16
        self.lookup['u32'] = TokenList.pt_u32
        self.lookup['u64'] = TokenList.pt_u64
        self.lookup['i8'] = TokenList.pt_i8
        self.lookup['i16'] = TokenList.pt_i16
        self.lookup['i32'] = TokenList.pt_i32
        self.lookup['i64'] = TokenList.pt_i64
        self.lookup['f32'] = TokenList.pt_float
        self.lookup['f64'] = TokenList.pt_double
        #Symbols
        self.lookup['!'] = TokenList.sym_not
        self.lookup['!='] = TokenList.sym_not_equal
        self.lookup['@'] = TokenList.sym_at
        self.lookup['#'] = TokenList.sym_hash
        #self.lookup['$'] = TokenList.sym_dollar
        self.lookup['%'] = TokenList.sym_remainder
        self.lookup['%='] = TokenList.sym_assign_remain
        self.lookup['^'] = TokenList.sym_xor
        self.lookup['^='] = TokenList.sym_assign_xor
        self.lookup['&'] = TokenList.sym_and
        self.lookup['&='] = TokenList.sym_assign_and
        self.lookup['*'] = TokenList.sym_asterisk
        self.lookup['*='] = TokenList.sym_assign_multiply
        self.lookup['('] = TokenList.sym_paren_open
        self.lookup[')'] = TokenList.sym_paren_close
        self.lookup['-'] = TokenList.sym_minus
        self.lookup['--'] = TokenList.sym_minus_one
        self.lookup['-='] = TokenList.sym_assign_subtract
        self.lookup['+'] = TokenList.sym_add
        self.lookup['++'] = TokenList.sym_plus_one
        self.lookup['+='] = TokenList.sym_assign_add
        self.lookup['='] = TokenList.sym_assign
        self.lookup['=='] = TokenList.sym_equal
        self.lookup['{'] = TokenList.sym_brace_open
        self.lookup['}'] = TokenList.sym_brace_close
        self.lookup['['] = TokenList.sym_bracket_open
        self.lookup[']'] = TokenList.sym_bracket_close
        self.lookup['|'] = TokenList.sym_or
        self.lookup['|='] = TokenList.sym_assign_or
        self.lookup['/'] = TokenList.sym_divide
        self.lookup['/='] = TokenList.sym_assign_divide
        self.lookup[';'] = TokenList.sym_semicolon
        self.lookup['<'] = TokenList.sym_less
        self.lookup['<='] = TokenList.sym_less_equal
        self.lookup['<<'] = TokenList.sym_shift_left
        self.lookup['>'] = TokenList.sym_greater
        self.lookup['>='] = TokenList.sym_greater_equal
        self.lookup['>>'] = TokenList.sym_shift_right
        self.lookup[','] = TokenList.sym_comma
        
        #self.lookup['=>'] = TokenList.sym_flow
        #self.lookup['?'] = TokenList.sym_question
    
    def SetInput(self, code):
        self.cursor = 0
        self.line = 1
        self.col = 0
        self.code = code

    def Ended(self):
        return True if self.cursor >= len(self.code)-1 else False

    def NextChar(self):
        """
        Get next character from the code
        return next character
        return 0 when no more character left

        """
        if self.Ended():
            return 0
        c = self.code[self.cursor]
        self.col += 1
        if c == '\n':
            self.line += 1
            self.col = 1
        self.cursor += 1
        return c

    def Lex(self):
        toks = []
        while not self.Ended():
            toks.append(self.GetNextToken())
        return toks
    
    def GetNextToken(self):
        #Skip comment
        while self.SkipCommentIfNeeded():
            # while current character is space
            while str.isspace(self.code[self.cursor]) or self.code[self.cursor] == '\n':
                self.NextChar()
                
        #Skip spaces
        while str.isspace(self.code[self.cursor]) or self.code[self.cursor] == '\n':
            self.NextChar()

        #Detect EOF
        if self.Ended() or self.code[self.cursor] == '\0':
            return None
        
        #if it is a alphabit character or a underscore
        if str.isalpha(self.code[self.cursor]) or self.code[self.cursor] == '_':
            return self.GetIdentifierToken()

        #if it is a number
        if str.isnumeric(self.code[self.cursor]):
            return self.GetNumbericToken()
        
        #if it is a symbol
        if not str.isalnum(self.code[self.cursor]) and self.code[self.cursor] != '_':
            # if it is a quote
            if self.code[self.cursor] == '\"' or self.code[self.cursor] == '\'':
                return self.GetStringToken()
            else:
                return self.GetSymbolToken()
    
    def SkipCommentIfNeeded(self):
        # if it is a space, that mean we have to skip it
        if str.isspace(self.code[self.cursor]) or self.code[self.cursor] == '\n':
            return True
        # if it is not what we looking for, then return false
        if self.code[self.cursor] != '/':
            return False

        unsure_symbol = ''
        #collect symbols
        while not self.Ended():
            if str.isspace(self.code[self.cursor]) \
            or str.isalnum(self.code[self.cursor]):
                break
            unsure_symbol += self.NextChar()
        
        # if that is a single-line comment
        if unsure_symbol == '//':
            # collect and skipping the comment
            while self.code[self.cursor] != '\n' and not self.Ended():
                self.NextChar()
            return True
        return False
    
    def GetPackedPos(self, offset=0):
        return (self.line, self.col-offset)

    def GetIdentifierToken(self):
        ident = ''
        # collect identifier
        # while (Not ended) and (not symbol except '_') 
        while not self.Ended() \
        and (str.isalnum(self.code[self.cursor]) or self.code[self.cursor] == '_'):
            ident += self.NextChar()

        #if it is in the lookup list
        if ident in self.lookup:
            return Token(self.lookup[ident], self.GetPackedPos())
        #it is just a identifer 
        return Token(TokenList.identifier, self.GetPackedPos(), TokenDataType.string, ident)

    def GetNumbericToken(self):
        num_text = ''
        dec_filter = re.compile(dec_pattern)
        float_filter = re.compile(float_pattern)
        hex_filter = re.compile(hex_pattern)
        bin_filter = re.compile(bin_pattern)

        while not self.Ended():
            if (not str.isalnum(self.code[self.cursor]) and self.code[self.cursor] != '.') or str.isspace(self.code[self.cursor]):
                break
            num_text += self.NextChar()

        if float_filter.match(num_text):
            # it is a floating
            try:
                return Token(TokenList.float_literal, self.GetPackedPos(len(num_text)), TokenDataType.floating, float(num_text))
            except ValueError:
                raise SyntaxError('Fail to fetch a float from text: "{}"'.format(num_text), self.GetPackedPos(len(num_text)))  
        elif dec_filter.match(num_text):
            # it is a decimal number
            try:
                # try to convert decimal into integer
                return Token(TokenList.int_literal, self.GetPackedPos(len(num_text)), TokenDataType.integer, int(num_text, 10))
            except ValueError:
                raise SyntaxError('Fail to fetch a integer from text: "{}"'.format(num_text), self.GetPackedPos(len(num_text)))  
        elif hex_filter.match(num_text):
            # it is a heximal number
            try:
                # attempt to convert heximal into integer
                return Token(TokenList.int_literal, self.GetPackedPos(len(num_text)), TokenDataType.integer, int(num_text, 16))
            except ValueError:
                raise SyntaxError('Fail to fetch a integer from text: "{}"'.format(num_text), self.GetPackedPos(len(num_text))) 
        elif bin_filter.match(num_text):
            # it is a binary number        
            try:
                # attempt to convert binary into integer
                return Token(TokenList.int_literal, self.GetPackedPos(len(num_text)), TokenDataType.integer, int(num_text[:-1], 2))
            except ValueError:
                raise SyntaxError('Fail to fetch a integer from text: "{}"'.format(num_text), self.GetPackedPos(len(num_text))) 
        else:
            raise SyntaxError('Unknown type of number: "{}"'.format(num_text), self.GetPackedPos(len(num_text)))

    def GetStringToken(self):
        text = ''
        quote = self.code[self.cursor]

        while(not self.Ended()):
            current = self.NextChar()

            if self.code[self.cursor] != quote:
                if current == '\\':
                    seek = self.NextChar()
                    simple_match = {'n':'\n',
                     'r':'\r', 
                     '0':'\0', 
                     't':'\t', 
                     '\\':seek, 
                     '\'':seek, 
                     '"':seek
                     }
                     # buggy
                    current = simple_match[seek]
                text += current
            else:
                break
        return Token(TokenList.str_literal, (self.line, self.col - len(text)), TokenDataType.string, text)    

    def GetSymbolToken(self):
        unsure_symbol = ''
        #collect symbol
        while not self.Ended():
            if str.isspace(self.code[self.cursor]) or str.isalnum(self.code[self.cursor]):
                break
            unsure_symbol += self.NextChar()
        
        #if we got a unknown symbol
        if not (unsure_symbol in self.lookup):
            #try search with single symbol
            single = self.code[self.cursor]

            if not (single in self.lookup):
                raise SyntaxError("Unknown symbol: {}".format(single.encode('utf-8')), self.GetPackedPos())
            else:
                unsure_symbol = single
        return Token(self.lookup[unsure_symbol], self.GetPackedPos())

if __name__ == '__main__':
    # Test function here
    print('### Lexer test ###')

    lexer = Lexer()

    print('* Comment ---------- ', end='')
    comment_code = '// message here\n\0'
    lexer.code = comment_code
    while not lexer.Ended():
        print(lexer.GetNextToken())

    print('* Function ---------- ', end='')
    print('* Statment ---------- ', end='')
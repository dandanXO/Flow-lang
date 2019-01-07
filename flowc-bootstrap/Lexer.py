from tokens import TokenList, Token, TokenDataType
import re

dec_pattern = r'\d+'
float_pattern = r'(?:\d+)?\.(\d+)'
hex_pattern = r'0x[0-9a-fA-F]*'
bin_pattern = r'\b([10]+)b\b'

class Lexer:
    """
        Lexer
        Generate token from code
        =========================
        file    Processed code file object
    """
    def __init__(self, file):
        self.fp = file
        self.line = 1
        self.col = 1
        self.curr_char = str()

        self.lookup = {}

        #Keywords
        self.lookup['nil'] = TokenList.kw_nil
        self.lookup['for'] = TokenList.kw_for
        self.lookup['in'] = TokenList.kw_in
        self.lookup['loop'] = TokenList.kw_loop
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
        self.lookup['filter'] = TokenList.kw_filter
        #self.lookup['func'] = TokenList.kw_func
        # self.lookup['static'] = TokenList.kw_static
        # self.lookup['const'] = TokenList.kw_const
        # self.lookup['struct'] = TokenList.kw_struct

        #Primitive types
        self.lookup['let'] = TokenList.pt_let
        self.lookup['ptr'] = TokenList.pt_ptr
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
        self.lookup['~'] = TokenList.sym_range
        self.lookup['~='] = TokenList.sym_included_range
        #self.lookup['=>'] = TokenList.sym_flow
        #self.lookup['?'] = TokenList.sym_not_sure

    # Destructor
    def __del__(self):
        self.fp.close()

    def reachedEnd(self):
        return True if self.curr_char == '' else False

    def nextChar(self):
        """
        Get next character from file
        return next character
        return 0 when no more character left

        """
        c = self.fp.read(1)
        self.curr_char = c
        #reached EOF
        if c == '':
            return c
        self.col += 1
        #if it is newline
        if c == '\n':
            self.line += 1
            self.col = 1
        return c

    def getNextToken(self):
        self.nextChar()
        #Skip comment
        self.skipIfNeeded()
        #if it is a alphabit character or a underscore
        if str.isalpha(self.curr_char) or self.curr_char == '_':
            return self.getIdentifierToken()

        #if it is a number
        if str.isnumeric(self.curr_char):
            return self.getNumbericToken()
        
        #if it is a symbol
        if not str.isalnum(self.curr_char) and self.curr_char != '_':
            # if it is a quote
            if self.curr_char == '\"' or self.curr_char == '\'':
                return self.getStringToken()
            elif self.curr_char != '':
                return self.GetSymbolToken()
        #if none of them match, return None
        return None
    
    def skipIfNeeded(self):
        # if it is a space, that mean we have to skip it
        while not self.reachedEnd() and str.isspace(self.curr_char):
            self.nextChar()
        while self.curr_char == '\n' and not self.reachedEnd():
            self.nextChar()
    
    def getCurrPos(self, offset=0):
        col = self.col-offset-1
        return (self.line, 1 if col < 1 else col)

    def getIdentifierToken(self):
        ident = str()
        # collect identifier
        # while (Not ended) and (not symbol except '_') 
        while not self.reachedEnd() \
        and (str.isalnum(self.curr_char) or self.curr_char == '_'):
            ident += self.curr_char
            self.nextChar()

        #if it is in the lookup list
        if ident in self.lookup:
            return Token(self.lookup[ident], self.getCurrPos(len(ident)))
        #it is just a identifer 
        return Token(TokenList.identifier, self.getCurrPos(len(ident)), TokenDataType.string, ident)

    def getNumbericToken(self):
        num_text = str()
        dec_checker = re.compile(dec_pattern)
        float_checker = re.compile(float_pattern)

        while not self.reachedEnd():
            if (not str.isalnum(self.curr_char) and self.curr_char != '.') or str.isspace(self.curr_char):
                break
            num_text += self.curr_char
            self.nextChar()
        print(self.curr_char)

        if float_checker.match(num_text):
            try:
                return Token(TokenList.float_literal, self.getCurrPos(len(num_text)), TokenDataType.floating, float(num_text))
            except ValueError:
                raise SyntaxError('Unable to fetch a float from text: "{}"'.format(num_text), self.getCurrPos(len(num_text)))  
        elif dec_checker.match(num_text):
            # it is a decimal number
            try:
                # try to convert num_text to a integer
                return Token(TokenList.int_literal, self.getCurrPos(len(num_text)), TokenDataType.integer, int(num_text, 10))
            except ValueError:
                raise SyntaxError('Unable to fetch an integer from text: "{}"'.format(num_text), self.getCurrPos(len(num_text)))  
        else:
            raise SyntaxError('Unknown type of number: "{}"'.format(num_text), self.getCurrPos(len(num_text)))

    def getStringToken(self):
        text = str()
        quote = self.curr_char

        while not self.reachedEnd():
            current = self.nextChar()
            if self.curr_char != quote:
                if current == '\\':
                    seek = self.nextChar()
                    if seek == 'n':
                        current = '\n'
                    if seek == 'r':
                        current = '\r'
                    if seek == '0':
                        current = '\0'
                    if seek == 't':
                        current = '\t'
                text += current
            else:
                break
        return Token(TokenList.str_literal, (self.line, self.col - len(text)), TokenDataType.string, text)    

    def GetSymbolToken(self):
        unsure_symbol = str()
        single = self.curr_char
        #collect symbol
        while not self.reachedEnd():
            if str.isspace(self.curr_char) or str.isalnum(self.curr_char):
                break
            unsure_symbol += self.curr_char
            self.nextChar()
        #if we got a unknown symbol
        if not (unsure_symbol in self.lookup):
            #try search with single symbol
            if not (single in self.lookup):
                raise RuntimeError("Syntax Error! Unknown symbol: {} At line {}".format(single.encode('utf-8'), self.getCurrPos()))
            else:
                unsure_symbol = single
        return Token(self.lookup[unsure_symbol], self.getCurrPos())


if __name__ == '__main__':
    lex = Lexer(open('test/lexer.text.flo', 'r', encoding='utf-8'))

    tok = lex.getNextToken()
    while tok != None:
        print(tok)
        tok = lex.getNextToken()
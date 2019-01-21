from enum import Enum, unique

@unique
class TokenList(Enum):
    # Keywords
    kw_nil = 'nil'
    kw_for = 'for'
    kw_in = 'in'
    kw_loop = 'loop'
    kw_continue = 'continue'
    kw_break = 'break'
    kw_if = 'if'
    kw_else = 'else'
    kw_not = 'not'
    kw_or = 'or'
    kw_xor = 'xor'
    kw_and = 'and'
    kw_true = 'true'
    kw_false = 'false'
    kw_while = 'while'
    kw_return = 'return'
    kw_filter = 'filter'
    kw_static = 'static'
    kw_const = 'const'
    kw_struct = 'struct'
    kw_func = 'func'
    kw_stack = '$tack'
    kw_stack_size = '$ize'
    # Types
    pt_let = 'let'
    pt_ptr = 'ptr'
    pt_bool = 'bool'
    pt_u8 = 'u8'
    pt_u16 = 'u16'
    pt_u32 = 'u32'
    pt_u64 = 'u64'
    pt_i8 = 'i8'
    pt_i16 = 'i16'
    pt_i32 = 'i32'
    pt_i64 = 'i64'  
    pt_float = 'f32'
    pt_double = 'f64'
    # Operators
    sym_not = '!'
    sym_not_equal = '!='
    # sym_at = '@'
    sym_hash = '#'
    sym_dollar = '$'
    sym_remainder = '%'
    sym_assign_remain = '%='
    sym_xor = '^'
    sym_assign_xor = '^='
    sym_and = '&'
    sym_assign_and = '&='
    sym_asterisk = '*'
    sym_assign_multiply = '*='
    sym_paren_open = '('
    sym_paren_close = ')'
    sym_minus = '-'
    sym_minus_one = '--'
    sym_assign_subtract = '-='
    sym_add = '+'
    sym_plus_one = '++'
    sym_assign_add = '+='
    sym_assign = '='
    sym_equal = '=='
    sym_brace_open = '{'
    sym_brace_close = '}'
    sym_bracket_open = '['
    sym_bracket_close = ']'
    sym_or = '|'
    sym_assign_or = '|='
    sym_divide = '/'
    sym_assign_divide = '/='
    sym_semicolon = ';'
    sym_less = '<'
    sym_less_equal = '<='
    sym_shift_left = '<<'
    sym_greater = '>'
    sym_greater_equal = '>='
    sym_shift_right = '>>'
    sym_comma = ','
    sym_range = '~'

    identifier = 'Identifier'
    # Literals
    str_literal = 'StringLiteral'
    float_literal = 'FloatLiteral'
    int_literal = 'IntegerLiteral'

PTYPE_TOKENS = [
    TokenList.pt_let, 
    TokenList.pt_ptr,
    TokenList.pt_bool, 
    TokenList.pt_double, 
    TokenList.pt_float, 
    TokenList.pt_i8, 
    TokenList.pt_i16, 
    TokenList.pt_i32, 
    TokenList.pt_i64, 
    TokenList.pt_u8,
    TokenList.pt_u16,
    TokenList.pt_u32,
    TokenList.pt_u64
]

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
        return 'Token {} {} at line {} : from col {} to {}'.format(self.id.value, data_msg, self.pos[0], self.pos[1], self.pos[2])
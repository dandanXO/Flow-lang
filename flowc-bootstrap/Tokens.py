
# Reserved word
TokenReserveds = {
    'nil': 'kw_nil', 
    'for': 'kw_for', 
    'in': 'kw_in', 
    'loop': 'kw_loop',
    'continue': 'kw_continue', 
    'break': 'kw_break', 
    'if': 'kw_if', 
    'else': 'kw_else',
    'not': 'kw_not',
    'or': 'kw_or', 
    'xor': 'kw_xor', 
    'and': 'kw_and',
    'true': 'kw_true', 
    'false': 'kw_false', 
    'while': 'kw_while', 
    'return': 'kw_return',
    'match': 'kw_match', 
    'const': 'kw_const', 
    'struct': 'kw_struct', 
    'func': 'kw_func', 
    'stack': 'kw_stack', 
    'let': 'kw_let'
    }

# Primitive types
TokenTypes = {
    'ptr': 'pt_ptr', 
    'bool': 'pt_bool', 
    'u8': 'pt_u8', 
    'u16': 'pt_u16', 
    'u32': 'pt_u32', 
    'u64': 'pt_u64', 
    'i8': 'pt_i8', 
    'i16': 'pt_i16', 
    'i32': 'pt_i32', 
    'i64': 'pt_i64', 
    'f32': 'pt_f32', 
    'f64': 'pt_f64'
    }

# Operators
TokenOperators = (\
    # !, !=, @
    'sym_not', 'sym_not_equal', 'sym_at', \
    # $, %, %=, ^
    'sym_dollar', 'sym_remainder', 'sym_assign_remain', 'sym_xor', \
    # ^=, &, &=, *
    'sym_assign_xor', 'sym_and', 'sym_assign_and', 'sym_asterisk', \
    # *=, (, ), -
    'sym_assign_multiply', 'sym_paren_open', 'sym_paren_close', 'sym_minus', \
    # --, -=, +, ++
    'sym_minus_one', 'sym_assign_subtract', 'sym_add', 'sym_plus_one', \
    # +=, =, ==, [
    'sym_assign_add', 'sym_assign', 'sym_equal', 'sym_brace_open', \
    # ], {, }, |
    'sym_brace_close', 'sym_bracket_open', 'sym_bracket_close', 'sym_or', \
    # |=, /, /=, ;
    'sym_assign_or', 'sym_divide', 'sym_assign_divide', 'sym_semicolon', \
    # <, <=, <<, <<=
    'sym_less', 'sym_less_equal', 'sym_shift_left', 'sym_assign_shift_left', \
    # >, >=, >>, >>=
    'sym_greater', 'sym_greater_equal', 'sym_shift_right', 'sym_assign_shift_right', \
    # , ~
    'sym_comma', 'sym_range') 

# Shapeless tokens
TokenShapeless = ('IDENTIFIER', 'STR_LITERAL', 'FLOAT_LITERAL', 'INT_LITERAL')

# Contain all tokens
TokenList = TokenReserveds + TokenTypes + TokenOperators + TokenShapeless
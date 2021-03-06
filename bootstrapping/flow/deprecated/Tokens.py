
# Reserved word
TokenReserveds = {
    'loop': 'KW_LOOP',
    'while': 'KW_WHILE',
    'continue': 'KW_CONTINUE', 
    'break': 'KW_BREAK', 
    'if': 'KW_IF', 
    'else': 'KW_ELSE',
    'elif': 'KW_ELIF',
    'not': 'KW_NOT',
    'or': 'KW_OR', 
    'xor': 'KW_XOR', 
    'and': 'KW_AND',
    'true': 'KW_TRUE', 
    'false': 'KW_FALSE', 
    'return': 'KW_RETURN',
    'const': 'KW_CONST', 
    'func': 'KW_FUNC', 
    'let': 'KW_LET',
    # Types
    'bool': 'PT_BOOL', 
    'u8': 'PT_U8', 
    'u16': 'PT_U16', 
    'u32': 'PT_U32', 
    'u64': 'PT_U64', 
    'i8': 'PT_I8', 
    'i16': 'PT_I16', 
    'i32': 'PT_I32', 
    'i64': 'PT_I64', 
    }

# Operators
TokenOperators = {\
    # !, !=, @, :
    '!': 'SYM_NOT', 
    '!=': 'SYM_NOT_EQUAL', 
    # '@': 'SYM_AT', 
    # ':': 'SYM_COLON',

    # $, %, %=, ^
    # '$': 'SYM_DOLLAR', 
    '%': 'SYM_REMAINDER', 
    '%=': 'SYM_ASSIGN_REMAINDER', 
    '^': 'SYM_XOR',

    # ^=, &, &=, *
    '^=': 'SYM_ASSIGN_XOR', 
    '&': 'SYM_AND', 
    '&=': 'SYM_ASSIGN_AND', 
    '*': 'SYM_ASTERISK',

    # *=, (, ), -
    '*=': 'SYM_ASSIGN_MULTIPLY', 
    '(': 'SYM_PAREN_OPEN', 
    ')': 'SYM_PAREN_CLOSE', 
    '-': 'SYM_MINUS',

    # --, -=, +, ++
    '--': 'SYM_MINUS_ONE', 
    '-=': 'SYM_ASSIGN_SUBTRACT', 
    '+': 'SYM_ADD', 
    '++': 'SYM_PLUS_ONE',

    # +=, =, ==, [
    '+=': 'SYM_ASSIGN_PLUS', 
    '=': 'SYM_ASSIGN', 
    '==': 'SYM_EQUAL', 
    # '[': 'SYM_BRACE_OPEN',

    # ], {, }, |
    # ']': 'SYM_BRACE_CLOSE', 
    '{': 'SYM_BRACKET_OPEN', 
    '}': 'SYM_BRACKET_CLOSE', 
    '|': 'SYM_OR',

    # |=, /, /=, ;
    '|=': 'SYM_ASSIGN_OR', 
    '/': 'SYM_DIVIDE', 
    '/=': 'SYM_ASSIGN_DIVIDE', 
    # ';': 'SYM_SEMICOLON',

    # <, <=, <<, <<=
    '<': 'SYM_LESS', 
    '<=': 'SYM_LESS_EQUAL', 
    '<<': 'SYM_SHIFT_LEFT', 
    '<<=': 'SYM_ASSIGN_SHIFT_LEFT',

    # >, >=, >>, >>=
    '>': 'SYM_GREATER', 
    '>=': 'SYM_GREATER_EQUAL', 
    '>>': 'SYM_SHIFT_RIGHT', 
    '>>=': 'SYM_ASSIGN_SHIFT_RIGHT',

    # , ~
    ',': 'SYM_COMMA', 
    # '~': 'SYM_RANGE'
}

# Shapeless tokens
TokenShapeless = [
    'IDENTIFIER', 
    # 'STR_LITERAL', 
    # 'CHAR_LITERAL', 
    # 'FLOAT_LITERAL', 
    'INT_LITERAL']

# Contain all tokens
TokenList = list(TokenReserveds.values()) + list(TokenOperators.values()) + TokenShapeless

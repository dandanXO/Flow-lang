from Tokens import TokenList
import ply.lex as plex

tokens = TokenList

# matching order: str_pattern >> 
# bin_pattern >> hex_pattern >> 
# float_pattern >> dec_pattern
dec_pattern = r'^[^\'\"\n0]\d+'
float_pattern = r'(?:\d+)?\.(\d+)'
hex_pattern = r'0x[^\s]([0-9a-f]*|[0-9A-F]*)'
bin_pattern = r'([10]+)b'
str_pattern = r'\"([^\\\n]|(\\.))*?\"'
comment_pattern = r'#\w+'

# Keywords
def t_IDENTIFIER(t):
    r"[_a-zA-Z][\w]*"
    
    return t



# Unit test
if __name__ == '__main__':
    print('Unit Test: Lexer')
    #create lexer
    lex = plex.lex()

#include "scanner.h"

Scanner::Scanner(string _code) {
    code = _code;
    cursor = 0;
    //line start from 1
    line = col = 1;
    /*
     * Register tokens
     * */
    // Keyword
    //since 1.0
    token_lookup.insert(pair<string, TokenType>("nil", KW_nil));
    token_lookup.insert(pair<string, TokenType>("for", KW_for));
    token_lookup.insert(pair<string, TokenType>("in", KW_in));
    token_lookup.insert(pair<string, TokenType>("continue", KW_continue));
    token_lookup.insert(pair<string, TokenType>("break", KW_break));
    token_lookup.insert(pair<string, TokenType>("if", KW_if));
    token_lookup.insert(pair<string, TokenType>("else", KW_else));
    token_lookup.insert(pair<string, TokenType>("not", KW_not));
    token_lookup.insert(pair<string, TokenType>("or", KW_or));
    token_lookup.insert(pair<string, TokenType>("xor", KW_xor));
    token_lookup.insert(pair<string, TokenType>("and", KW_and));
    token_lookup.insert(pair<string, TokenType>("true", KW_true));
    token_lookup.insert(pair<string, TokenType>("false", KW_false));
    token_lookup.insert(pair<string, TokenType>("while", KW_while));
    token_lookup.insert(pair<string, TokenType>("return", KW_return));
    // Types
    //since 1.0
    token_lookup.insert(pair<string, TokenType>("bool", PTY_bool));
    token_lookup.insert(pair<string, TokenType>("u8", PTY_u8));
    token_lookup.insert(pair<string, TokenType>("u16", PTY_u16));
    token_lookup.insert(pair<string, TokenType>("u32", PTY_u32));
    token_lookup.insert(pair<string, TokenType>("u64", PTY_u64));
    token_lookup.insert(pair<string, TokenType>("i8", PTY_i8));
    token_lookup.insert(pair<string, TokenType>("i16", PTY_i16));
    token_lookup.insert(pair<string, TokenType>("i32", PTY_i32));
    token_lookup.insert(pair<string, TokenType>("i64", PTY_i64));
    // Operators
    //since 1.0
    token_lookup.insert(pair<string, TokenType>("!", SYM_not));
    token_lookup.insert(pair<string, TokenType>("!=", SYM_not_equal));
    token_lookup.insert(pair<string, TokenType>("%", SYM_remainder));
    token_lookup.insert(pair<string, TokenType>("%=", SYM_remain_assign));
    token_lookup.insert(pair<string, TokenType>("^", SYM_xor));
    token_lookup.insert(pair<string, TokenType>("^=", SYM_xor_assign));
    token_lookup.insert(pair<string, TokenType>("&", SYM_and));
    token_lookup.insert(pair<string, TokenType>("&=", SYM_and_assign));
    token_lookup.insert(pair<string, TokenType>("*", SYM_asterisk));
    token_lookup.insert(pair<string, TokenType>("*=", SYM_multiply_assign));
    token_lookup.insert(pair<string, TokenType>("(", SYM_parenthesis_open));
    token_lookup.insert(pair<string, TokenType>(")", SYM_parenthesis_close));
    token_lookup.insert(pair<string, TokenType>("-", SYM_minus));
    token_lookup.insert(pair<string, TokenType>("--", SYM_minus_one));
    token_lookup.insert(pair<string, TokenType>("-=", SYM_subtract_assign));
    token_lookup.insert(pair<string, TokenType>("+", SYM_plus));
    token_lookup.insert(pair<string, TokenType>("++", SYM_add_one));
    token_lookup.insert(pair<string, TokenType>("+=", SYM_add_assign));
    token_lookup.insert(pair<string, TokenType>("=", SYM_assign));
    token_lookup.insert(pair<string, TokenType>("==", SYM_equal));
    token_lookup.insert(pair<string, TokenType>("{", SYM_brace_open));
    token_lookup.insert(pair<string, TokenType>("}", SYM_brace_close));
    token_lookup.insert(pair<string, TokenType>("[", SYM_bracket_open));
    token_lookup.insert(pair<string, TokenType>("]", SYM_bracket_close));
    token_lookup.insert(pair<string, TokenType>("|", SYM_or));
    token_lookup.insert(pair<string, TokenType>("|=", SYM_or_assign));
    token_lookup.insert(pair<string, TokenType>("/", SYM_divide));
    token_lookup.insert(pair<string, TokenType>("/=", SYM_divide_assign));
    token_lookup.insert(pair<string, TokenType>(";", SYM_semicolon));
    token_lookup.insert(pair<string, TokenType>("<", SYM_less_than));
    token_lookup.insert(pair<string, TokenType>("<=", SYM_less_equal));
    token_lookup.insert(pair<string, TokenType>("<<", SYM_shift_left));
    token_lookup.insert(pair<string, TokenType>(">", SYM_greater_than));
    token_lookup.insert(pair<string, TokenType>(">=", SYM_greater_equal));
    token_lookup.insert(pair<string, TokenType>(">>", SYM_shift_right));
    token_lookup.insert(pair<string, TokenType>(",", SYM_comma));

}

char Scanner::NextChar() {
    if (Ended()) return 0x0;
    char c = code[cursor];
    col++;
    if (c == '\r' or c == '\n') {
        line++;
        col = 1;
    }
    cursor++;
    return c;
}

void Scanner::PrintLocation(uint32_t length) {
    printf("[Scanner] Col %d at line %d : \n", col - length, line);
}

unique_ptr<Token> Scanner::GetNextToken() {

    //skipping comments
    while (SkipCommentIfNeeded()) {
        //Skip spaces while we skipping the limitless comments
        while (isspace(code[cursor])) NextChar();
    }

    //Skip spaces
    while (isspace(code[cursor])) NextChar();

    if (code[cursor] == '\0' or Ended())
        return make_unique<Token>(Token(EndOfFile, line, col, ""));

    //if it is a alpha character or a underscore
    if (isalpha(code[cursor]) or code[cursor] == '_') {
        return GetIdentifierTok();
    }
    //if it is a number
    if (isdigit(code[cursor])) {
        return GetNumberTok();
    }
    //if it is a symbol
    if (not isalnum(code[cursor]) and code[cursor] != '_') {
        //but if it is a quote
        if (code[cursor] == '"' || code[cursor] == '\'') {
            return GetStringTok();
        } else {
            return GetSymbolTok();
        }
    }
}

bool Scanner::SkipCommentIfNeeded() {
    //If it is a space, that mean we have to skip it
    if (isspace(code[cursor])) return true;
    //If not what we looking for, then return.
    if (code[cursor] != '/') return false;
    string unsure_symbol, comment_text;
    //collect symbol
    while (not Ended()) {
        if (isspace(code[cursor]) or isalnum(code[cursor])) {
            break;
        }
        unsure_symbol += NextChar();
    }

    //If that is a single line comment
    if (unsure_symbol == "//") {
        //skip it until we reach the newline
        while (code[cursor] != '\n' and not Ended()) {
            comment_text += NextChar();
        }
        printf("Skipped a single line comment: \"%s\"\n", comment_text.c_str());
        //maybe more of it
        return true;
    }
        //If that's a multi line comment
    else if (unsure_symbol == "/*") {
        //find a '*'
        while (code[cursor] != '*' and not Ended()) {
            comment_text += NextChar();
        }
        //once we found it
        if (code[cursor] == '*') {
            //see if the next character is a '/'
            if (code[cursor + 1] == '/' and not Ended()) {
                //it is.
                NextChar();
                NextChar();
                printf("Skipped a multi line comment: \"\n%s\"\n", comment_text.c_str());
                //maybe more of it
                return true;
            }
        }
        //error msg
        PrintLocation(0);
        printf("\t[SkipCommentIfNeeded] Multi line comment symbol doesn't paired!\n");
        exit(-1);
    }
}

unique_ptr<Token> Scanner::GetIdentifierTok() {
    string ident;
    TokenType unsure_tok;

    do {
        ident += NextChar();
    }
        //while (Not ended) and (not space) and (not symbol except '_')
    while (not Ended() && !isspace(code[cursor]) && (isalnum(code[cursor]) || code[cursor] == '_'));

    //Identifier as default
    unsure_tok = TokenType::Identifier;

    auto result = token_lookup.find(ident);
    //if we found a keyword
    if (result != token_lookup.end()) {
        return make_unique<Token>(token_lookup[ident], line, col - ident.size(), "");
    }
    //just a identifier

    return make_unique<Token>(Identifier, line, col - ident.size(), ident);
}

unique_ptr<Token> Scanner::GetStringTok() {
    string text;
    //save quote_type
    char quote_type = code[cursor];

    do {
        char current = NextChar();
        //if we met the end of the string
        if (code[cursor] != quote_type) {
            //handle control characters and quotes
            if (current == '\\') {
                char next = NextChar();

                //NOTICE: The special characters in code is different to the actual ASCII code!
                switch (next) {
                    //if newline found
                    case 'n':
                        current = '\n'; // 0xa in ASCII
                        break;

                        //if return found
                    case 'r':
                        current = '\r'; // 0xd in ASCII
                        break;

                        //if null found
                    case '0':
                        current = '\0'; // 0x0 in ASCII
                        break;

                        //if tab found
                    case 't':
                        current = '\t'; // 0x9 in ASCII
                        break;

                        //if backslash found
                    case '\\':
                        //just a normal backslash

                        //if single quote found
                    case '\'':

                        //if double quote found
                    case '"':
                        //same.
                        current = next;
                        break;

                    default:
                        //If none of these matched, that mean it is a bad backslash
                        PrintLocation(1);
                        printf("\t[GetStringTok] I can't reconize a control characters after blackslash!\n");
                        printf("\t\tReceived: 0x%x (ASCII:%c)\n", next, next);
                        exit(-1);
                        break;
                }
            }
            text += current;
        } else {
            break;
        }
    }
        //while (not ended) and (not the right quote type)
    while (not Ended());

    //if it is empty, zero it
    if (text.length() == 0) {
        text += '\0';
    }

    return make_unique<Token>(StringLiteral, line, col - text.size(), text);
}

unique_ptr<Token> Scanner::GetNumberTok() {
    string num_text;
    //regexs
    regex dec_check(DECIMAL_REGEX);
    regex float_check(FLOAT_REGEX);
//    regex hex_check(HEXIMAL_REGEX);
//    regex bin_check(BINARY_REGEX);

    // 1. Collect much characters as we can
    while (not Ended()) {
        if ((!isalnum(code[cursor]) and code[cursor] != '.') or isspace(code[cursor])) {
            break;
        }
        num_text += NextChar();
    }
    // 2. Validate and get type of the number using regex.
    //
    if (regex_match(num_text, dec_check)) {
        //It is a decimal number
        uint64_t val;
        istringstream iss(num_text);
        iss >> val;
        return make_unique<Token>(DecimalLiteral, line, col - num_text.size(), val);
    } else if (regex_match(num_text, float_check)) {
        //It is a float number
        return make_unique<Token>(FloatLiteral, line, col - num_text.size(), stod(num_text));
    }
    // TODO: Implement Heximal and binary number
//    else if (regex_match(num_text, hex_check))
//    {
//        //It is a heximal number
//        tok_content = num_text;
//        return HeximalLiteral;
//    }
//    else if (regex_match(num_text, bin_check))
//    {
//        //It is a binary
//        tok_content = num_text;
//        return BinaryLiteral;
//    }
    //Cannot reconize what kind of number
    PrintLocation(num_text.size());
    printf("\t[GetNumberTok] Unknown type of number!\n");
    printf("\t\tReceived: %s\n", num_text.c_str());
    exit(-1);

}

unique_ptr<Token> Scanner::GetSymbolTok() {
    string unsure_symbol;
    //collect symbol
    while (not Ended()) {
        if (isspace(code[cursor]) or isalnum(code[cursor])) {
            break;
        }
        unsure_symbol += NextChar();
    }

    //search for the current symbol(s)
    auto result = token_lookup.find(unsure_symbol);
    //if not found
    if (result == token_lookup.end()) {
        //just try to search single character
        string single;
        single += code[cursor];
        //if not found
        if (token_lookup.find(single) == token_lookup.end()) {
            //error msg
            PrintLocation(unsure_symbol.size());
            printf("\t[GetSymbolTok] Unknown symbol!\n");
            printf("\t\tReceived: %s (0x%x)\n", unsure_symbol.c_str(), unsure_symbol[0]);
            exit(-1);
        }
        //else
        unsure_symbol = single;
    }

    return make_unique<Token>(token_lookup[unsure_symbol], line, col - unsure_symbol.size(), "");
}


#pragma once

#include <string>
#include <memory>
#include <variant>
#include <iostream>

using namespace std;

const string IDENTIFIER_REGEX = "\\b[^\'\"0-9][_0-9a-zA-Z]+[^\'\"]\\b";
const string STRING_REGEX = "[\"].+[\"]|[\'].+[\']|('')|("")";
const string FLOAT_REGEX = "(?:\\d+)?(?:\\.?\\d*)";
const string DECIMAL_REGEX = "\\b[0-9]+\\b";
const string HEXIMAL_REGEX = "0x[0-9a-fA-F]*";
const string BINARY_REGEX = "\\b([10]+)b\\b";
const string SYMBOL_REGEX = "[^\\w\\s]";

//Make sure this array is aligned to TokenType
const string Token2Text[] = {
        "EndOfFile",
        /*
            Keywords
        */
        "nil",
        "for",
        "in",
        "continue",
        "break",
        "if",
        "else",
        "not",
        "or",
        "xor",
        "and",
        "true",
        "false",
        "while",
        "return",
        //types
        "bool",
        "u8",
        "u16",
        "u32",
        "u64",
        "i8",
        "i16",
        "i32",
        "i64",
        /*
            Operators
        */
        "!",
        "!=",
        "%",
        "%=",
        "^",
        "^=",
        "&",
        "&=",
        "*",
        "*=",
        "(",
        ")",
        "-",
        "--",
        "-=",
        "+",
        "++",
        "+=",
        "=",
        "==",
        "{",
        "}",
        "[",
        "]",
        "|",
        "|=",
        "/",
        "/=",
        ";",
        "<",
        "<=",
        "<<",
        ">",
        ">=",
        ">>",
        ",",


        "Identifier",
        /*
            Literal
        */
        "StringLiteral",
        "FloatLiteral",
        "DecimalLiteral",
        "HeximalLiteral",
        "BinaryLiteral",
};

enum TokenType {
    EndOfFile = 0,
    /*
        Keywords
    */
            KW_nil,
    KW_for,
    KW_in,
    KW_continue,
    KW_break,
    KW_if,
    KW_else,
    KW_not,
    KW_or,
    KW_xor,
    KW_and,
    KW_true,
    KW_false,
    KW_while,
    KW_return,
    //types
            PTY_bool,
    PTY_u8,
    PTY_u16,
    PTY_u32,
    PTY_u64,
    PTY_i8,
    PTY_i16,
    PTY_i32,
    PTY_i64,
    /*
        Operators
    */
    // !
            SYM_not,
    // !=
            SYM_not_equal,
    // %
            SYM_remainder,
    // %=
            SYM_remain_assign,
    // ^
            SYM_xor,
    // ^=
            SYM_xor_assign,
    // &
            SYM_and,
    // &=
            SYM_and_assign,
    // *
            SYM_asterisk,
    // *=
            SYM_multiply_assign,
    // (
            SYM_parenthesis_open,
    // )
            SYM_parenthesis_close,
    // -
            SYM_minus,
    // --
            SYM_minus_one,
    // -=
            SYM_subtract_assign,
    // +
            SYM_plus,
    // ++
            SYM_add_one,
    // +=
            SYM_add_assign,
    // =
            SYM_assign,
    // ==
            SYM_equal,
    // {
            SYM_brace_open,
    // }
            SYM_brace_close,
    // [
            SYM_bracket_open,
    // ]
            SYM_bracket_close,
    // |
            SYM_or,
    // |=
            SYM_or_assign,
    // /
            SYM_divide,
    // /=
            SYM_divide_assign,
    // ;
            SYM_semicolon,
    // <
            SYM_less_than,
    // <=
            SYM_less_equal,
    // <<
            SYM_shift_left,
    // >
            SYM_greater_than,
    //>=
            SYM_greater_equal,
    // >>
            SYM_shift_right,
    // ,
            SYM_comma,

    Identifier,
    /*
        Literal
    */
            StringLiteral,
    FloatLiteral,
    DecimalLiteral,
    HeximalLiteral,
    BinaryLiteral,
};

class Token {
    TokenType id;
    uint32_t line;
    uint32_t col;
    variant<string, uint64_t, double> content;

    struct pri_dump {
        void operator()(const string &c) {
            cout << c;
        }

        void operator()(const uint64_t &c) {
            cout << c;
        }

        void operator()(const double &c) {
            cout << c;
        }
    };

public:
    // Constructor with string type content
    Token(TokenType _tok, uint32_t _line, uint32_t _col, string _content) : \
    id(_tok), line(_line), col(_col), content(_content) {}

    // Constructor with integer type content
    Token(TokenType _tok, uint32_t _line, uint32_t _col, uint64_t _content) : \
    id(_tok), line(_line), col(_col), content(_content) {}

    // Constructor with double type content
    Token(TokenType _tok, uint32_t _line, uint32_t _col, double _content) : \
    id(_tok), line(_line), col(_col), content(_content) {}

    // Position
    uint32_t GetLine() { return line; }

    uint32_t GetCol() { return col; }

    // Dump data
    void Dump() {
        printf("Line: %d | ", line);
        printf("Col: %d | ", col);
        printf("Token: %s (%d) | ", Token2Text[id].c_str(), id);
        printf("Content: ");
        visit(pri_dump(), content);
        printf("\n");
    }

};
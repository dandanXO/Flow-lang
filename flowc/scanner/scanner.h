#pragma once

#include "tokens.h"

#include <string>
#include <vector>
#include <regex>
#include <iostream>
#include <map>
#include <memory>


using namespace std;

class Scanner {
public:
    Scanner(string _code);

    unique_ptr<Token> GetNextToken();

    bool Ended() { return cursor >= code.size() - 1 ? true : false; }

    void DumpTokens() {
        while (not Ended()) {
            GetNextToken()->Dump();
        }
    }

private:
    string code;
    uint32_t cursor;
    uint32_t line;
    uint32_t col;
    map<string, TokenType> token_lookup;

    bool SkipCommentIfNeeded();

    unique_ptr<Token> GetIdentifierTok();

    unique_ptr<Token> GetStringTok();

    unique_ptr<Token> GetNumberTok();

    unique_ptr<Token> GetSymbolTok();

    char NextChar();

    void PrintLocation(uint32_t length);
};



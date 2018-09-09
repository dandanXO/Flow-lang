#pragma once

#include <memory>
#include "scanner/scanner.h"

using namespace std;

class Parser{
    public:
        Parser(unique_ptr<Scanner> scanner) : sc(move(scanner)){}
        
    private:
        unique_ptr<Scanner> sc;
};
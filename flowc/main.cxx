
#include <iostream>
#include <fstream>
#include "flow.h"

using namespace std;

int main(int argc, char *args[]) {
    string code;
    if (argc == 1) {
        printf("No input file.\n");
        return -1;
    }
    char *path = args[1];
    string line;
    ifstream file(path);
    if (file) {
        while (getline(file, line)) {
            code += line + '\n';
        }

    } else {
        printf("Cannot open file: %s\n", path);
        return -1;
    }
    //release the file
    file.close();

    Scanner scanner(code);
    scanner.DumpTokens();
    printf("ENDED");
    return 0;
}
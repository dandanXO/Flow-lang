# The Flow programming language

Flow is a multi-purpose programming language, aimed to create a highly flexible and unified programming language.

**What Flow can do?**

You can compile Flow code to a excutable file or run it on interpreter, that mean you can compile your script to executable file or debugging hardware driver with graphical programming environment. 

Thats impressive isn't it?

**Bootstrapping**
The bootstrap compiler will be written in pure python, with several python libraries. The goal here is self-lifting. 

 - [ ] Multiple file compilation
 - [ ] C FFI
 - [ ] Basic SSL

**Milestones**

2. Compiling <-> Interpreting

## Compiler Architecture
**Preprocessing**

Purify source code and resovle preprocessing variables
Workflow:
1. Gathering host infomation(platform, target, current directory, output directory, passed arguments)
2. Build ```env``` table
3. Resolve external project(git, ftp)

**Lexer**

Extracting tokens from processed source code using PLY


**Parser**

Generate AST from stream of tokens using PLY

**Code Generation**

**Synchronice Standard Library(SSL)**

A flexible standard library that constantly update itself.

Everytime you compiling SSL's code, and it will update the SSL functions you currently have.

Protocol of SSL functions(function name, return type, parameters) will be unified by Flow Language community. For improving SSL, users can write their own version of SSL functions, and submit it to the SSL Repository, then admins will pick the most efficient one that users submitted, and patch it into next SSL update. Simplily, this is a competetive way to improve the quality of the SSL.

The compiler and all libraries is fully open-source.
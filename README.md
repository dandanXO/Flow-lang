# The Flow programming language

Flow is a multi-purpose programming language, aimed to create a highly flexible and unified programming language.

**What Flow can do?**

You can compile Flow code to a excutable file or run it on interpreter, that mean you can compile your script to executable file or debugging hardware driver with graphical programming environment. 

Thats impressive isn't it?

**Bootstrapping**
The bootstrap compiler will be written in pure python, with several python libraries. The goal is self-lifting. 

 - [ ] Multiple file compilation
 - [ ] C FFI
 - [ ] Basic SSL

**Milestones**

2. Compiling <-> Interpreting

## Architecture
**Preprocessing**

Generate source code base on the environment variables.
Workflow:
1. Gathering host infomation(platform, target, current directory, output directory, passed arguments)
2. Build ```env``` table
3. Resolve external project(git, ftp)
**Lexing**
Extracting tokens from processed source code

****
**AST Builder**

**Code Generation**

**Synchronice Standard Library(SSL)**

A flexible standard library that constantly update itself.

The compiler will check if there is a update of SSL functions everytime you compiling SSL's code, and will update the SSL functions you currently have.

Protocol of SSL functions(function name, return type, parameters) will be unified by Flow Language editors. For improving the SSL, users can write their own version of SSL functions, and submit it to the SSL server, then the server will pick the most efficient one and replace currently use one with the faster one. Basiclly, this is a competetive way to improve the quality of the SSL.

The library is fully open-source.
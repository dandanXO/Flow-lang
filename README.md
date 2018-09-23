# The Flow programming language

Flow is a multi-purpose programming language, aimed to create a highly flexible and unified programming language.

**What Flow can do?**

You can compile Flow code to a excutable file or run it on interpreter, that mean you can compile your script to executable file or debugging hardware driver with graphical programming environment. 

Thats impressive isn't it?

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
==========================================
    Warning! Grammer and typos ahead!
==========================================


Workflow of flowc-beta
===========================
1. gathering info
    * read build.json in workspace
2. read text from IO
    * file:
        * method 1: preload file to memory - "Currently use"
        * method 2: read character every NextChar() - "Better efficient"
    * stream: read character from buffer
3. lexing
    * one by one: get token by calling GetNextToken() - "Currently use, bad for peeking but efficient"
    * token array: an array of all tokens - "poor memory efficient but good for peeking"
4. parser
    * 
5. type checking

6. code generation

7. compile IR
    * invoke llc: good enouf

Program properties
===========================

* program entry
The entry point of Flow code is a file, 'main.flo' by default. It can also be changed by specified entry point in 'build.json'. 
Code inside the entry file(entry point in general speaking) is simplily equal to the content inside 'int main()' in C/C++, it gives better view of the main flow which usually showed how the program work. 
Ofcause in most application, we will have to use arguments and return value of main function to receving arguments from the shell and feedback status, Flow's standard library provides related functionalities to get the job done.

* better varies argument

                    STACK VIEW
-------------------------------------------------------
                    return address
-------------------------------------------------------
            number of pushed arguments
        (should be known at compile time)    
-------------------------------------------------------
    length and type(integer or pointer) of 1st argument
-------------------------------------------------------
                    1st argument
-------------------------------------------------------
    length and type(integer or pointer) of nth argument
-------------------------------------------------------
                    nth argument
-------------------------------------------------------

number of pushed arguments: 1 byte(127 max)

length and type field
+--------------+
|  0  | 1 ~ 7  |
| type| length |
+--------------+
type:
    0: integer
    1: pointer
length:
    0: invalid
    1~127: length in byte

* exception handle

Declare function with 'responsive', 
and caller must implement an error handler
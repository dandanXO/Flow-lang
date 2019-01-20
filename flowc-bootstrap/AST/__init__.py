from llvmlite import ir
from enum import Enum, unique
from Tokens import TokenList

@unique
class BinaryOperation(Enum):
    Addition = 1
    Subtract = 2
    Multiply = 3
    Divide = 4
    Remain = 5

    Not = 6
    Or = 7
    And = 8
    Xor = 9
    Shl = 10
    Shr = 11


@unique
class PrimitiveDataType(Enum):
    void = 0
    boolean = 1
    u8 = 2
    u16 = 3
    u32 = 4
    u64 = 5
    i8 = 6
    i16 = 7
    i32 = 8
    i64 = 9
    f32 = 10
    f64 = 11
    string = 12
    pointer = 13
    

class ASTBase:
    def __init__(self, name, pos):
        self.name = name
        self.line = pos[0]
        self.col = pos[1]

    def GrowTree(self, module, builder, resources):
        return None
        
    def __str__(self):
        return "{} @ ({}, {})\n\t".format(self.name, self.line, self.col)
from enum import Enum, unique

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
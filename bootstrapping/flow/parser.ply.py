from Lexer import Lexer
from Tokens import TokenList
import ply.yacc as yacc

from AST.BinOpNode import BinOpNode
from AST.BranchNode import IfBranchNode
from AST.FlowCtrlNode import ContinueNode
from AST.FunctionNode import FunctionCall, FunctionHeaderNode, FunctionNode
from AST.UnaryNode import UnaryNode
from AST.VariableNode import VariableDeclareNode


class Parser:
    def __init__(self, initial_scope):
        self.precedence = (
            ('left', '<<', '>>'),
            ('left', '|', '&', '^'),
            ('left', '+', '-'),
            ('left', '*', '/'),
            ('right', 'UNARY')
        )

    def build(self, text, **args):
        self.parser = yacc.parse(lexer=Lexer(text=text))
    
    #############################################################
    #                       Actual Syntax
    #############################################################

    def p_expression_BinOp(self, p):
        '''
            expression : expression arithmetic expression
                        | expression compareOp expression
                        | expression KW_OR expression
                        | expression KW_XOR expression
                        | expression KW_AND expression
        '''
        p[0] = BinOpNode(p[1], p[2], p[3])

    def p_expression_unary(self, p):
        '''
            expression : SYM_NOT expression %prec UNARY
                       | SYM_MINUS expression %prec UNARY
                       | KW_NOT expression %prec UNARY
        '''
        p[0] = UnaryNode(p[1], p[2])

    def p_statement_func_call(self, p):
        '''
            statement : IDENTIFIER SYM_PAREN_OPEN multi_values SYM_PAREN_CLOSE
                      | IDENTIFIER SYM_PAREN_OPEN SYM_PAREN_CLOSE
        '''
        #call with empty argument
        if len(p) == 4:
            p[0] = FunctionCall(p[1], [])
        else:
            #with arguments
            p[0] = FunctionCall(p[1], p[3])
    
    def p_statement_var_decl(self, p):
        '''
            statement : type IDENTIFIER SYM_ASSIGN expression
                        | modifier type IDENTIFIER SYM_ASSIGN expression
                        | KW_LET IDENTIFIER SYM_ASSIGN expression
        '''
        #with modifier
        if len(p) == 6:
            if p[1] == 'const':
                p[0] = VariableDeclareNode(p[3], p[2], p[5], False)
        else:
            p[0] = VariableDeclareNode(p[2], p[1], p[4], True)

    def p_statement_multi_var_decl(self, p):
        '''
            statement : type multi_var_assign
                        | modifier type multi_var_assign
                        | KW_LET multi_var_assign
        '''

    def p_statement_branch(self, p):
        '''
            statement : if_statement
                        | if_statement elif_statement
                        | if_statement else_statement
                        | if_statement elif_statement else_statement
        '''

    def p_if_statement(self, p):
        '''
            if_statement : KW_IF expression scope_statement
        '''
        p[0] = IfBranchNode(p[2], p[3])

    def p_elif_statement(self, p):
        '''
            elif_statment : KW_ELIF expression scope_statement
                        | elif_statment elif_statement
        '''


    def p_else_statement(self, p):
        'else_statement : KW_ELSE scope_statement'
        p[0] = p[2]

    def p_statement_scope(self, p):
        '''
            scope_statement : SYM_BRACKET_OPEN SYM_BRACKET_CLOSE
                            | SYM_BRACKET_OPEN statement SYM_BRACKET_CLOSE
        '''

    #############################################################
    #                       Routines
    #############################################################
    def p_statement(self, p):
        'statement : expression'
        p[0] = p[1]

    def p_multi_var_assign(self, p):
        '''
            multi_var_assign : multi_idents SYM_ASSIGN multi_values
                        | multi_idents SYM_ASSIGN expression
        '''
        # single variable
        p[0] = [p[1], p[3]]

    def p_modifier(self, p):
        'modifier : KW_CONST'
        p[0] = p[1]

    def p_expression_paren(self, p):
        'expression : SYM_PAREN_OPEN expression SYM_PAREN_CLOSE'
        p[0] = p[2]

    def p_value(self, p):
        '''
            expression : INT_LITERAL
                       | KW_TRUE
                       | KW_FALSE
        '''
        if p[1] == 'true':
            p[0] = 1
        elif p[1] == 'false':
            p[0] = 0
        else:
            p[0] = p[1]

    def p_arithmetic(self, p):
        '''
            arithmetic : SYM_REMAINDER
                       | SYM_XOR
                       | SYM_AND
                       | SYM_ASTERISK
                       | SYM_MINUS
                       | SYM_ADD
                       | SYM_OR
                       | SYM_DIVIDE
                       | SYM_SHIFT_LEFT
                       | SYM_SHIFT_RIGHT
        '''
        p[0] = p[1]

    def p_compareOp(self, p):
        '''
            compareOp : SYM_EQUAL
                        | SYM_NOT_EQUAL
                        | SYM_LESS
                        | SYM_LESS_EQUAL
                        | SYM_GREATER
                        | SYM_GREATER_EQUAL
        '''
        p[0] = p[1]

    #assemble expressions
    def p_multi_values(self, p):
        '''
            multi_values : expression SYM_COMMA
                        | expression SYM_COMMA multi_values
        '''
        if len(p) == 3:
            #first syntax
            p[0] = [p[1]]
        else:
            # second syntax
            p[0] = [p[1]] + p[3] # append all the elements into a single list

    #assemble identifiers
    def p_multi_idents(self, p):
        '''
            multi_idents : IDENTIFIER SYM_COMMA
                    | IDENTIFIER SYM_COMMA multi_idents
        '''
        if len(p) == 3 or len(p) == 2:
            #first syntax
            p[0] = [p[1]]
        else:
            # second syntax
            p[0] = [p[1]] + p[3] # append all the elements into a single list

    def p_type(self, p):
        '''
            type : PT_BOOL
                 | PT_U8
                 | PT_U16
                 | PT_U32
                 | PT_U64
                 | PT_I8
                 | PT_I16
                 | PT_I32
                 | PT_I64
        '''
        p[0] = p[1]

if __name__ == '__main__':
    pass


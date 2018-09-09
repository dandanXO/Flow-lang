#pragma once

#include "llvm/IR/Value.h"
#include <cctype>
#include <string>
#include <vector>
#include <variant>

using namespace std;

enum OperatorType {
    Plus = 1,
    Subtract,
    Multiply,
    Divide,
    Remainder,
    Not,
    Or,
    And,
    Xor,
    Equal,
    NotEqual,
    Greater,
    Less,
    GreaterEqual,
    LessEqual,
};

/*
    Nodes
*/
class ExpressionNode {
public:
    virtual ~ExpressionNode();

    virtual llvm::Value *codegen() = 0;
};

class IdentifierDeclBlock : public ExpressionNode {
public:
    IdentifierDeclBlock(string _name) : name(_name) {}

    llvm::Value *codegen() override;

private:
    string name;
};

class LiteralBlock : public ExpressionNode {
public:
    LiteralBlock(string _val) : value(_val) {}

    LiteralBlock(uint64_t _val) : value(_val) {}

    LiteralBlock(double _val) : value(_val) {}

    llvm::Value *codegen() override;

private:
    variant<string, uint64_t, double> value;
};

class VariableDeclBlock : public ExpressionNode {
public:
    VariableDeclBlock(unique_ptr<IdentifierDeclBlock> _ident, unique_ptr<ExpressionNode> _exp) : \
    ident(move(_ident)), expression(move(_exp)) {}

    llvm::Value *codegen() override;

private:
    unique_ptr<IdentifierDeclBlock> ident;
    unique_ptr<ExpressionNode> expression;
};

class BinaryOpBlock : public ExpressionNode {
public:
    BinaryOpBlock(OperatorType _op, unique_ptr<ExpressionNode> _lhs, unique_ptr<ExpressionNode> _rhs) : \
    op(_op), lhs(move(_lhs)), rhs(move(_rhs)) {}

    llvm::Value *codegen() override;

private:
    OperatorType op;
    unique_ptr<ExpressionNode> lhs;
    unique_ptr<ExpressionNode> rhs;
};

class IfBranchBlock : public ExpressionNode {
public:
    IfBranchBlock(unique_ptr<BinaryOpBlock> _condit, unique_ptr<ExpressionNode> _then, unique_ptr<ExpressionNode> _else)
            : \
    condition(move(_condit)), then_block(move(_then)), else_block(move(_else)) {}

    llvm::Value *codegen() override;

private:
    unique_ptr<BinaryOpBlock> condition;
    unique_ptr<ExpressionNode> then_block;
    unique_ptr<ExpressionNode> else_block;
};

class ScopeBlock : public ExpressionNode {

};

class FunctionBlock : public ExpressionNode {
public:
    FunctionBlock() {}

    llvm::Value *codegen() override;

private:
    string name;
    bool varies_arg;
    bool external;
    unique_ptr<IdentifierDeclBlock> func_ident;
    unique_ptr<ExpressionNode> return_block;
    unique_ptr<ExpressionNode> body;
    vector<unique_ptr<IdentifierDeclBlock>> param_types;
    vector<string> params;
};

class AssignBlock : public ExpressionNode {
public:
    AssignBlock() {}

    llvm::Value *codegen() override;

private:

};

class FuncCallBlock : public ExpressionNode {
public:
    FuncCallBlock() {}

    llvm::Value *codegen() override;

private:

};

class ContinueBlock : public ExpressionNode {
public:
    ContinueBlock() {}

    llvm::Value *codegen() override;

private:

};

class BreakBlock : public ExpressionNode {
public:
    BreakBlock() {}

    llvm::Value *codegen() override;

private:

};


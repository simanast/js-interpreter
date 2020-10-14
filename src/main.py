import sys
from antlr4 import *
from JavaScriptLexer import JavaScriptLexer
from AstVisitor import *

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = JavaScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaScriptParser(stream)
    tree = parser.program()

    visitor = AstVisitor()
    visitor.visit(tree=tree)
    print(visitor.tree)


if __name__ == '__main__':
    main(sys.argv)

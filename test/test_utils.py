from antlr4 import *
from src.JavaScriptLexer import JavaScriptLexer
from src.AstVisitor import *
import os


def getTree(path: str):
    input_stream = FileStream(path)
    lexer = JavaScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaScriptParser(stream)
    tree = parser.program()

    visitor = AstVisitor()
    visitor.visit(tree=tree)
    return visitor.tree


def readTreeFromFile(path: str):
    tree = ''
    f = open(path)
    for line in f:
        tree += line
    f.close()
    return tree


def isOutFile(filename: str):
    return filename[-4:] == ".out"


def getJsFileName(out_file: str):
    string = out_file[:-4] + ".js"
    return string


def getFilenames(path: str):
    path = os.path.join(os.getcwd(), path)
    filenames = []
    for file in os.listdir(path):
        if isOutFile(file):
            filenames.append(file[:-4])
    return filenames


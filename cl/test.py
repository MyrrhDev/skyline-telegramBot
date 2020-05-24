import sys
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from TreeVisitor import TreeVisitor
from EvalVisitor import EvalVisitor


input_stream = InputStream(input('? '))

lexer = SkylineLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SkylineParser(token_stream)
tree = parser.root()


print(tree.toStringTree(recog=parser))

visitor = TreeVisitor()
visitor.visit(tree)


#visitor = EvalVisitor()
#visitor.visit(tree)

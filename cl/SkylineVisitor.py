# Generated from Skyline.g4 by ANTLR 4.7.2
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from cl.SkylineParser import SkylineParser


# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx: SkylineParser.RootContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#assign.
    def visitAssign(self, ctx: SkylineParser.AssignContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#skyExp.
    def visitSkyExp(self, ctx: SkylineParser.SkyExpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#rightExp.
    def visitRightExp(self, ctx: SkylineParser.RightExpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#parentesisExp.
    def visitParentesisExp(self, ctx: SkylineParser.ParentesisExpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#multExp.
    def visitMultExp(self, ctx: SkylineParser.MultExpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#leftExp.
    def visitLeftExp(self, ctx: SkylineParser.LeftExpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#unionExp.
    def visitUnionExp(self, ctx: SkylineParser.UnionExpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#interExp.
    def visitInterExp(self, ctx: SkylineParser.InterExpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#reflectExp.
    def visitReflectExp(self, ctx: SkylineParser.ReflectExpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#sky.
    def visitSky(self, ctx: SkylineParser.SkyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#crea.
    def visitCrea(self, ctx: SkylineParser.CreaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#multcrea.
    def visitMultcrea(self, ctx: SkylineParser.MultcreaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#aleatorio.
    def visitAleatorio(self, ctx: SkylineParser.AleatorioContext):
        return self.visitChildren(ctx)


del SkylineParser

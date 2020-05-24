if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class TreeVisitor(SkylineVisitor):
    def __init__(self):
        self.nivel = 0

    #Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        if ctx.getChildCount() == 1:
            n = next(ctx.getChildren())
            print(" " * self.nivel + 
                  SkylineParser.symbolicNames[n.getSymbol().type] + 
                  '(' +n.getText() + ')')
            self.nivel -= 1
        elif ctx.getChildCount() == 3:
            print(' ' * self.nivel + 'MES (+)')
            self.nivel +=1
            self.visit(ctx.expr(0))
            self.nivel +=1
            self.visit(ctx.expr(1))

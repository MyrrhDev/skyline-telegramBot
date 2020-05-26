# Generated from Skyline.g4 by ANTLR 4.7.2
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor

else:
    from cl.SkylineParser import SkylineParser
    from cl.SkylineVisitor import SkylineVisitor

from skyline import Skyline as sk


# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class EvalVisitor(SkylineVisitor):
    def __init__(self, user_data):
        print('init')
        self.user_data = user_data

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx: SkylineParser.RootContext):
        n = next(ctx.getChildren())
        print('root')
        return self.visit(n)

    # Visit a parse tree produced by SkylineParser#assign.
    def visitAssign(self, ctx: SkylineParser.AssignContext):
        print('assign')
        l = [n for n in ctx.getChildren()]
        # ID
        id = l[0].getText()
        print(id)

        # sky: para guardar en la ts
        # y se devuelve sky para hacer el plot en bot.py
        # TODO: se hace el update aqui de la tabla de simbolos?
        # TODO: tiene permanencia en bot.py si se cambia aqui
        #  o se tendria que hacer en bot.py
        if len(l) == 3:
            print('assign-next')
            sky = self.visit(l[2])
            print('back from sky')
            print(sky.get_height())
            self.user_data = sk.update_symbols(id, self.user_data, sky)
            return sky

    # Visit a parse tree produced by SkylineParser#skyExp.
    def visitSkyExp(self, ctx: SkylineParser.SkyExpContext):
        print('visitSkyExp')
        n = next(ctx.getChildren())
        return self.visit(n)

    # Visit a parse tree produced by SkylineParser#rightExp.
    def visitRightExp(self, ctx: SkylineParser.RightExpContext):
        l = [n for n in ctx.getChildren()]
        m_sky = self.visit(l[0])
        return m_sky.move_right((int(l[2].getText())))

    # Visit a parse tree produced by SkylineParser#parentesisExp.
    def visitParentesisExp(self, ctx: SkylineParser.ParentesisExpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#multExp.
    def visitMultExp(self, ctx: SkylineParser.MultExpContext):
        l = [n for n in ctx.getChildren()]
        m_sky = self.visit(l[0])
        print(int(l[2].getText()))
        (mult_sky_x, mult_sky_h, mult_sky_w) = m_sky.multiply_N(int(l[2].getText()))
        mult_skl = sk(0,0,0)
        mult_skl.c_skyline(mult_sky_x, mult_sky_h, mult_sky_w)
        return mult_skl

    # Visit a parse tree produced by SkylineParser#leftExp.
    def visitLeftExp(self, ctx: SkylineParser.LeftExpContext):
        l = [n for n in ctx.getChildren()]
        m_sky = self.visit(l[0])
        return m_sky.move_left((int(l[2].getText())))

    # Visit a parse tree produced by SkylineParser#unionExp.
    # TODO: Igual necesitare cambiar esto para la construccion aleatoria
    #  de skylines con "width"
    def visitUnionExp(self, ctx: SkylineParser.UnionExpContext):
        l = [n for n in ctx.getChildren()]
        m_sky = self.visit(l[0])
        n_sky = self.visit(l[2])
        (sm_x_pos, sm_heights, sm_width) = m_sky.sumar_skyline(n_sky.xmin, n_sky.height[0], n_sky.xmax)
        union_skl = sk(0,0,0)
        union_skl.c_skyline(sm_x_pos, sm_heights, sm_width)
        return union_skl

    # Visit a parse tree produced by SkylineParser#interExp.
    def visitInterExp(self, ctx: SkylineParser.InterExpContext):
        l = [n for n in ctx.getChildren()]
        f_sky = self.visit(l[0])
        s_sky = self.visit(l[2])
        (sm_x_pos, sm_heights, sm_width) = f_sky.inter_skyline(s_sky.xmin, s_sky.height[0], s_sky.xmax)
        inter_skl = sk(0,0,0)
        inter_skl.c_skyline(sm_x_pos, sm_heights, sm_width)
        return inter_skl

    # Visit a parse tree produced by SkylineParser#reflectExp.
    def visitReflectExp(self, ctx: SkylineParser.ReflectExpContext):
        l = [n for n in ctx.getChildren()]
        # visita l[1] para obtener el id o sky
        sky = self.visit(l[1])
        # y luego devuelve ese skyline reflected
        (r_x_pos, r_heights, r_width) = sky.reflect_skyline()
        reflect_skl = sk(0,0,0)
        reflect_skl.c_skyline(r_x_pos, r_heights, r_width)
        return reflect_skl

    # Visit a parse tree produced by SkylineParser#sky.
    def visitSky(self, ctx: SkylineParser.SkyContext):
        print('visitSky')
        l = [n for n in ctx.getChildren()]
        # true si es NUM, ID, etc...
        check = hasattr(l[0], 'getSymbol')
        # get ID
        if check:
            get_id = l[0].getText()  # "d"
            print(get_id)
            get_sky = sk.find_symbol(get_id, self.user_data)
            return get_sky
        # visitamos crea
        else:
            print('visitSky -else')
            return self.visit(l[0])

    # Visit a parse tree produced by SkylineParser#crea.
    def visitCrea(self, ctx: SkylineParser.CreaContext):
        print('visitCrea')
        l = [n for n in ctx.getChildren()]
        if len(l) == 7:
            return sk(int(l[1].getText()), int(l[3].getText()), int(l[5].getText()))

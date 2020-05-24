# Generated from Skyline.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("F\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\5\2")
        buf.write("\17\n\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4\37\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\60\n\4\f\4\16\4\63\13")
        buf.write("\4\3\5\3\5\5\5\67\n\5\3\6\3\6\3\6\3\6\7\6=\n\6\f\6\16")
        buf.write("\6@\13\6\5\6B\n\6\3\6\3\6\3\6\2\3\6\7\2\4\6\b\n\2\2\2")
        buf.write("K\2\16\3\2\2\2\4\22\3\2\2\2\6\36\3\2\2\2\b\66\3\2\2\2")
        buf.write("\n8\3\2\2\2\f\17\5\4\3\2\r\17\5\6\4\2\16\f\3\2\2\2\16")
        buf.write("\r\3\2\2\2\17\20\3\2\2\2\20\21\7\2\2\3\21\3\3\2\2\2\22")
        buf.write("\23\7\f\2\2\23\24\7\3\2\2\24\25\5\6\4\2\25\5\3\2\2\2\26")
        buf.write("\27\b\4\1\2\27\30\7\4\2\2\30\31\5\6\4\2\31\32\7\5\2\2")
        buf.write("\32\37\3\2\2\2\33\37\5\b\5\2\34\35\7\6\2\2\35\37\5\6\4")
        buf.write("\b\36\26\3\2\2\2\36\33\3\2\2\2\36\34\3\2\2\2\37\61\3\2")
        buf.write("\2\2 !\f\7\2\2!\"\7\7\2\2\"\60\5\6\4\b#$\f\5\2\2$%\7\b")
        buf.write("\2\2%\60\5\6\4\6&\'\f\6\2\2\'(\7\7\2\2(\60\7\n\2\2)*\f")
        buf.write("\4\2\2*+\7\b\2\2+\60\7\n\2\2,-\f\3\2\2-.\7\6\2\2.\60\7")
        buf.write("\n\2\2/ \3\2\2\2/#\3\2\2\2/&\3\2\2\2/)\3\2\2\2/,\3\2\2")
        buf.write("\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\7\3\2\2")
        buf.write("\2\63\61\3\2\2\2\64\67\7\f\2\2\65\67\5\n\6\2\66\64\3\2")
        buf.write("\2\2\66\65\3\2\2\2\67\t\3\2\2\28A\7\4\2\29>\7\n\2\2:;")
        buf.write("\7\t\2\2;=\7\n\2\2<:\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2")
        buf.write("\2\2?B\3\2\2\2@>\3\2\2\2A9\3\2\2\2AB\3\2\2\2BC\3\2\2\2")
        buf.write("CD\7\5\2\2D\13\3\2\2\2\t\16\36/\61\66>A")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'('", "')'", "'-'", "'*'", "'+'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUM", "DIGIT", "ID", "LETTER", "WS" ]

    RULE_root = 0
    RULE_assign = 1
    RULE_expr = 2
    RULE_sky = 3
    RULE_crea = 4

    ruleNames =  [ "root", "assign", "expr", "sky", "crea" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NUM=8
    DIGIT=9
    ID=10
    LETTER=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def assign(self):
            return self.getTypedRuleContext(SkylineParser.AssignContext,0)


        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 10
                self.assign()
                pass

            elif la_ == 2:
                self.state = 11
                self.expr(0)
                pass


            self.state = 14
            self.match(SkylineParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = SkylineParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(SkylineParser.ID)
            self.state = 17
            self.match(SkylineParser.T__0)
            self.state = 18
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SkylineParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SkyExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sky(self):
            return self.getTypedRuleContext(SkylineParser.SkyContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkyExp" ):
                return visitor.visitSkyExp(self)
            else:
                return visitor.visitChildren(self)


    class RightExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)

        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRightExp" ):
                return visitor.visitRightExp(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesisExp" ):
                return visitor.visitParentesisExp(self)
            else:
                return visitor.visitChildren(self)


    class MultExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)

        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultExp" ):
                return visitor.visitMultExp(self)
            else:
                return visitor.visitChildren(self)


    class LeftExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)

        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeftExp" ):
                return visitor.visitLeftExp(self)
            else:
                return visitor.visitChildren(self)


    class UnionExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnionExp" ):
                return visitor.visitUnionExp(self)
            else:
                return visitor.visitChildren(self)


    class InterExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterExp" ):
                return visitor.visitInterExp(self)
            else:
                return visitor.visitChildren(self)


    class ReflectExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReflectExp" ):
                return visitor.visitReflectExp(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = SkylineParser.ParentesisExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 21
                self.match(SkylineParser.T__1)
                self.state = 22
                self.expr(0)
                self.state = 23
                self.match(SkylineParser.T__2)
                pass

            elif la_ == 2:
                localctx = SkylineParser.SkyExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.sky()
                pass

            elif la_ == 3:
                localctx = SkylineParser.ReflectExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(SkylineParser.T__3)
                self.state = 27
                self.expr(6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 45
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.InterExpContext(self, SkylineParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 31
                        self.match(SkylineParser.T__4)
                        self.state = 32
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.UnionExpContext(self, SkylineParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 34
                        self.match(SkylineParser.T__5)
                        self.state = 35
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.MultExpContext(self, SkylineParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 37
                        self.match(SkylineParser.T__4)
                        self.state = 38
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.RightExpContext(self, SkylineParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 40
                        self.match(SkylineParser.T__5)
                        self.state = 41
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 5:
                        localctx = SkylineParser.LeftExpContext(self, SkylineParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 43
                        self.match(SkylineParser.T__3)
                        self.state = 44
                        self.match(SkylineParser.NUM)
                        pass

             
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class SkyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)

        def crea(self):
            return self.getTypedRuleContext(SkylineParser.CreaContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_sky

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSky" ):
                return visitor.visitSky(self)
            else:
                return visitor.visitChildren(self)




    def sky(self):

        localctx = SkylineParser.SkyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sky)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(SkylineParser.ID)
                pass
            elif token in [SkylineParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.crea()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CreaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_crea

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCrea" ):
                return visitor.visitCrea(self)
            else:
                return visitor.visitChildren(self)




    def crea(self):

        localctx = SkylineParser.CreaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_crea)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(SkylineParser.T__1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SkylineParser.NUM:
                self.state = 55
                self.match(SkylineParser.NUM)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SkylineParser.T__6:
                    self.state = 56
                    self.match(SkylineParser.T__6)
                    self.state = 57
                    self.match(SkylineParser.NUM)
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 65
            self.match(SkylineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         





# Generated from Skyline.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("R\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\r\6\r<\n\r\r\r\16\r=\3\16\3\16")
        buf.write("\3\17\3\17\3\17\7\17E\n\17\f\17\16\17H\13\17\3\20\3\20")
        buf.write("\3\21\6\21M\n\21\r\21\16\21N\3\21\3\21\2\2\22\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22\3\2\4\4\2C\\c|\4\2\f\f\"\"\2U\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5&\3\2\2\2")
        buf.write("\7(\3\2\2\2\t*\3\2\2\2\13,\3\2\2\2\r.\3\2\2\2\17\60\3")
        buf.write("\2\2\2\21\62\3\2\2\2\23\64\3\2\2\2\25\66\3\2\2\2\278\3")
        buf.write("\2\2\2\31;\3\2\2\2\33?\3\2\2\2\35A\3\2\2\2\37I\3\2\2\2")
        buf.write("!L\3\2\2\2#$\7<\2\2$%\7?\2\2%\4\3\2\2\2&\'\7*\2\2\'\6")
        buf.write("\3\2\2\2()\7+\2\2)\b\3\2\2\2*+\7/\2\2+\n\3\2\2\2,-\7,")
        buf.write("\2\2-\f\3\2\2\2./\7-\2\2/\16\3\2\2\2\60\61\7.\2\2\61\20")
        buf.write("\3\2\2\2\62\63\7]\2\2\63\22\3\2\2\2\64\65\7_\2\2\65\24")
        buf.write("\3\2\2\2\66\67\7}\2\2\67\26\3\2\2\289\7\177\2\29\30\3")
        buf.write("\2\2\2:<\5\33\16\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2")
        buf.write("\2\2>\32\3\2\2\2?@\4\62;\2@\34\3\2\2\2AF\5\37\20\2BE\5")
        buf.write("\37\20\2CE\5\33\16\2DB\3\2\2\2DC\3\2\2\2EH\3\2\2\2FD\3")
        buf.write("\2\2\2FG\3\2\2\2G\36\3\2\2\2HF\3\2\2\2IJ\t\2\2\2J \3\2")
        buf.write("\2\2KM\t\3\2\2LK\3\2\2\2MN\3\2\2\2NL\3\2\2\2NO\3\2\2\2")
        buf.write("OP\3\2\2\2PQ\b\21\2\2Q\"\3\2\2\2\7\2=DFN\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    NUM = 12
    DIGIT = 13
    ID = 14
    LETTER = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'('", "')'", "'-'", "'*'", "'+'", "','", "'['", "']'", 
            "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "DIGIT", "ID", "LETTER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "NUM", "DIGIT", "ID", 
                  "LETTER", "WS" ]

    grammarFileName = "Skyline.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



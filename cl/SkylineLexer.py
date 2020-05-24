# Generated from Skyline.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("B\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\6\t,\n\t\r\t\16\t-\3\n\3\n\3\13\3\13\3\13\7\13")
        buf.write("\65\n\13\f\13\16\138\13\13\3\f\3\f\3\r\6\r=\n\r\r\r\16")
        buf.write("\r>\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\3\2\4\4\2C\\c|\4\2\f\f\"\"\2E\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2")
        buf.write("\2\5\36\3\2\2\2\7 \3\2\2\2\t\"\3\2\2\2\13$\3\2\2\2\r&")
        buf.write("\3\2\2\2\17(\3\2\2\2\21+\3\2\2\2\23/\3\2\2\2\25\61\3\2")
        buf.write("\2\2\279\3\2\2\2\31<\3\2\2\2\33\34\7<\2\2\34\35\7?\2\2")
        buf.write("\35\4\3\2\2\2\36\37\7*\2\2\37\6\3\2\2\2 !\7+\2\2!\b\3")
        buf.write("\2\2\2\"#\7/\2\2#\n\3\2\2\2$%\7,\2\2%\f\3\2\2\2&\'\7-")
        buf.write("\2\2\'\16\3\2\2\2()\7.\2\2)\20\3\2\2\2*,\5\23\n\2+*\3")
        buf.write("\2\2\2,-\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\22\3\2\2\2/\60\4")
        buf.write("\62;\2\60\24\3\2\2\2\61\66\5\27\f\2\62\65\5\27\f\2\63")
        buf.write("\65\5\23\n\2\64\62\3\2\2\2\64\63\3\2\2\2\658\3\2\2\2\66")
        buf.write("\64\3\2\2\2\66\67\3\2\2\2\67\26\3\2\2\28\66\3\2\2\29:")
        buf.write("\t\2\2\2:\30\3\2\2\2;=\t\3\2\2<;\3\2\2\2=>\3\2\2\2><\3")
        buf.write("\2\2\2>?\3\2\2\2?@\3\2\2\2@A\b\r\2\2A\32\3\2\2\2\7\2-")
        buf.write("\64\66>\3\b\2\2")
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
    NUM = 8
    DIGIT = 9
    ID = 10
    LETTER = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'('", "')'", "'-'", "'*'", "'+'", "','" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "DIGIT", "ID", "LETTER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "NUM", "DIGIT", "ID", "LETTER", "WS" ]

    grammarFileName = "Skyline.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



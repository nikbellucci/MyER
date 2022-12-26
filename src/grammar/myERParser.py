# Generated from src/grammar/myER.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,186,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,1,1,1,1,1,1,1,3,
        1,42,8,1,1,1,3,1,45,8,1,1,1,1,1,3,1,49,8,1,1,1,3,1,52,8,1,1,1,1,
        1,3,1,56,8,1,1,1,3,1,59,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,71,8,3,1,3,3,3,74,8,3,1,4,1,4,1,4,5,4,79,8,4,10,4,12,4,82,
        9,4,1,5,1,5,1,5,1,5,1,5,3,5,89,8,5,1,6,1,6,1,7,1,7,1,7,5,7,96,8,
        7,10,7,12,7,99,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,121,8,8,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,3,10,154,8,10,1,11,1,11,1,11,5,11,159,8,11,10,11,12,11,162,
        9,11,1,12,1,12,1,12,5,12,167,8,12,10,12,12,12,170,9,12,1,12,1,12,
        1,12,3,12,175,8,12,1,13,1,13,1,13,1,13,1,13,3,13,182,8,13,1,14,1,
        14,1,14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,3,1,0,2,
        3,1,0,6,11,1,0,17,18,203,0,34,1,0,0,0,2,37,1,0,0,0,4,60,1,0,0,0,
        6,64,1,0,0,0,8,75,1,0,0,0,10,88,1,0,0,0,12,90,1,0,0,0,14,92,1,0,
        0,0,16,120,1,0,0,0,18,122,1,0,0,0,20,153,1,0,0,0,22,155,1,0,0,0,
        24,174,1,0,0,0,26,181,1,0,0,0,28,183,1,0,0,0,30,33,3,2,1,0,31,33,
        3,6,3,0,32,30,1,0,0,0,32,31,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,
        34,35,1,0,0,0,35,1,1,0,0,0,36,34,1,0,0,0,37,38,5,1,0,0,38,44,5,34,
        0,0,39,41,5,23,0,0,40,42,3,8,4,0,41,40,1,0,0,0,41,42,1,0,0,0,42,
        43,1,0,0,0,43,45,5,24,0,0,44,39,1,0,0,0,44,45,1,0,0,0,45,48,1,0,
        0,0,46,47,7,0,0,0,47,49,3,14,7,0,48,46,1,0,0,0,48,49,1,0,0,0,49,
        51,1,0,0,0,50,52,3,4,2,0,51,50,1,0,0,0,51,52,1,0,0,0,52,55,1,0,0,
        0,53,54,5,4,0,0,54,56,3,14,7,0,55,53,1,0,0,0,55,56,1,0,0,0,56,58,
        1,0,0,0,57,59,5,26,0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,3,1,0,0,0,
        60,61,5,21,0,0,61,62,3,22,11,0,62,63,5,22,0,0,63,5,1,0,0,0,64,65,
        5,5,0,0,65,66,5,34,0,0,66,67,5,23,0,0,67,68,3,24,12,0,68,70,5,24,
        0,0,69,71,3,4,2,0,70,69,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,72,74,
        5,26,0,0,73,72,1,0,0,0,73,74,1,0,0,0,74,7,1,0,0,0,75,80,3,10,5,0,
        76,77,5,28,0,0,77,79,3,10,5,0,78,76,1,0,0,0,79,82,1,0,0,0,80,78,
        1,0,0,0,80,81,1,0,0,0,81,9,1,0,0,0,82,80,1,0,0,0,83,89,5,34,0,0,
        84,85,5,34,0,0,85,89,3,12,6,0,86,87,5,34,0,0,87,89,3,28,14,0,88,
        83,1,0,0,0,88,84,1,0,0,0,88,86,1,0,0,0,89,11,1,0,0,0,90,91,7,1,0,
        0,91,13,1,0,0,0,92,97,5,34,0,0,93,94,5,28,0,0,94,96,5,34,0,0,95,
        93,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,15,1,0,0,
        0,99,97,1,0,0,0,100,121,5,12,0,0,101,102,5,12,0,0,102,103,5,19,0,
        0,103,104,3,18,9,0,104,105,5,20,0,0,105,121,1,0,0,0,106,121,5,13,
        0,0,107,108,5,13,0,0,108,109,5,19,0,0,109,110,3,18,9,0,110,111,5,
        20,0,0,111,121,1,0,0,0,112,121,5,14,0,0,113,121,5,15,0,0,114,121,
        5,16,0,0,115,116,5,16,0,0,116,117,5,19,0,0,117,118,3,18,9,0,118,
        119,5,20,0,0,119,121,1,0,0,0,120,100,1,0,0,0,120,101,1,0,0,0,120,
        106,1,0,0,0,120,107,1,0,0,0,120,112,1,0,0,0,120,113,1,0,0,0,120,
        114,1,0,0,0,120,115,1,0,0,0,121,17,1,0,0,0,122,123,5,33,0,0,123,
        19,1,0,0,0,124,154,5,34,0,0,125,126,5,34,0,0,126,154,3,28,14,0,127,
        128,5,34,0,0,128,154,3,12,6,0,129,130,5,34,0,0,130,131,5,25,0,0,
        131,154,3,16,8,0,132,133,5,34,0,0,133,134,5,25,0,0,134,135,3,16,
        8,0,135,136,3,28,14,0,136,154,1,0,0,0,137,138,5,34,0,0,138,139,5,
        25,0,0,139,140,3,16,8,0,140,141,3,12,6,0,141,154,1,0,0,0,142,143,
        5,34,0,0,143,144,5,21,0,0,144,145,3,22,11,0,145,146,5,22,0,0,146,
        154,1,0,0,0,147,148,5,34,0,0,148,149,5,21,0,0,149,150,3,22,11,0,
        150,151,5,22,0,0,151,152,3,12,6,0,152,154,1,0,0,0,153,124,1,0,0,
        0,153,125,1,0,0,0,153,127,1,0,0,0,153,129,1,0,0,0,153,132,1,0,0,
        0,153,137,1,0,0,0,153,142,1,0,0,0,153,147,1,0,0,0,154,21,1,0,0,0,
        155,160,3,20,10,0,156,157,5,28,0,0,157,159,3,20,10,0,158,156,1,0,
        0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,23,1,0,0,
        0,162,160,1,0,0,0,163,168,3,26,13,0,164,165,5,28,0,0,165,167,3,26,
        13,0,166,164,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,
        0,0,169,175,1,0,0,0,170,168,1,0,0,0,171,172,3,26,13,0,172,173,5,
        30,0,0,173,175,1,0,0,0,174,163,1,0,0,0,174,171,1,0,0,0,175,25,1,
        0,0,0,176,182,5,34,0,0,177,178,5,34,0,0,178,182,3,12,6,0,179,180,
        5,34,0,0,180,182,3,28,14,0,181,176,1,0,0,0,181,177,1,0,0,0,181,179,
        1,0,0,0,182,27,1,0,0,0,183,184,7,2,0,0,184,29,1,0,0,0,19,32,34,41,
        44,48,51,55,58,70,73,80,88,97,120,153,160,168,174,181
    ]

class myERParser ( Parser ):

    grammarFileName = "myER.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ENTITY'", "'EXTENDS'", "'SPECIALIZES'", 
                     "'SPECIALIZED BY'", "'RELATION'", "'[0-1]'", "'[1-1]'", 
                     "'[1-N]'", "'[1-n]'", "'[0-N]'", "'[0-n]'", "'string'", 
                     "'integer'", "'boolean'", "'date'", "'float'", "'PK'", 
                     "'PRIMARY KEY'", "'['", "']'", "'{'", "'}'", "'('", 
                     "')'", "':'", "';'", "'.'", "','", "'-'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "LBRACKET", 
                      "RBRACKET", "LBRACE", "RBRACE", "LPAREN", "RPAREN", 
                      "COLON", "SEMICOLON", "DOT", "COMMA", "DASH", "REC", 
                      "Whitespace", "Newline", "Integer", "Identifier", 
                      "LineComment", "BlockComment" ]

    RULE_program = 0
    RULE_entityDeclaration = 1
    RULE_attributeBlock = 2
    RULE_relationDeclaration = 3
    RULE_relationSpecificationList = 4
    RULE_relationSpecification = 5
    RULE_multiplicity = 6
    RULE_identifierList = 7
    RULE_type = 8
    RULE_dataByte = 9
    RULE_attributeDeclaration = 10
    RULE_attributeDeclarationList = 11
    RULE_entitySpecificationList = 12
    RULE_entitySpecification = 13
    RULE_primaryKey = 14

    ruleNames =  [ "program", "entityDeclaration", "attributeBlock", "relationDeclaration", 
                   "relationSpecificationList", "relationSpecification", 
                   "multiplicity", "identifierList", "type", "dataByte", 
                   "attributeDeclaration", "attributeDeclarationList", "entitySpecificationList", 
                   "entitySpecification", "primaryKey" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    LBRACKET=19
    RBRACKET=20
    LBRACE=21
    RBRACE=22
    LPAREN=23
    RPAREN=24
    COLON=25
    SEMICOLON=26
    DOT=27
    COMMA=28
    DASH=29
    REC=30
    Whitespace=31
    Newline=32
    Integer=33
    Identifier=34
    LineComment=35
    BlockComment=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entityDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(myERParser.EntityDeclarationContext)
            else:
                return self.getTypedRuleContext(myERParser.EntityDeclarationContext,i)


        def relationDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(myERParser.RelationDeclarationContext)
            else:
                return self.getTypedRuleContext(myERParser.RelationDeclarationContext,i)


        def getRuleIndex(self):
            return myERParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = myERParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==5:
                self.state = 32
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 30
                    self.entityDeclaration()
                    pass
                elif token in [5]:
                    self.state = 31
                    self.relationDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(myERParser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(myERParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(myERParser.RPAREN, 0)

        def identifierList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(myERParser.IdentifierListContext)
            else:
                return self.getTypedRuleContext(myERParser.IdentifierListContext,i)


        def attributeBlock(self):
            return self.getTypedRuleContext(myERParser.AttributeBlockContext,0)


        def SEMICOLON(self):
            return self.getToken(myERParser.SEMICOLON, 0)

        def relationSpecificationList(self):
            return self.getTypedRuleContext(myERParser.RelationSpecificationListContext,0)


        def getRuleIndex(self):
            return myERParser.RULE_entityDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityDeclaration" ):
                listener.enterEntityDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityDeclaration" ):
                listener.exitEntityDeclaration(self)




    def entityDeclaration(self):

        localctx = myERParser.EntityDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entityDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(myERParser.T__0)
            self.state = 38
            self.match(myERParser.Identifier)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 39
                self.match(myERParser.LPAREN)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==34:
                    self.state = 40
                    self.relationSpecificationList()


                self.state = 43
                self.match(myERParser.RPAREN)


            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==3:
                self.state = 46
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 47
                self.identifierList()


            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 50
                self.attributeBlock()


            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 53
                self.match(myERParser.T__3)
                self.state = 54
                self.identifierList()


            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 57
                self.match(myERParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(myERParser.LBRACE, 0)

        def attributeDeclarationList(self):
            return self.getTypedRuleContext(myERParser.AttributeDeclarationListContext,0)


        def RBRACE(self):
            return self.getToken(myERParser.RBRACE, 0)

        def getRuleIndex(self):
            return myERParser.RULE_attributeBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeBlock" ):
                listener.enterAttributeBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeBlock" ):
                listener.exitAttributeBlock(self)




    def attributeBlock(self):

        localctx = myERParser.AttributeBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_attributeBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(myERParser.LBRACE)
            self.state = 61
            self.attributeDeclarationList()
            self.state = 62
            self.match(myERParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(myERParser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(myERParser.LPAREN, 0)

        def entitySpecificationList(self):
            return self.getTypedRuleContext(myERParser.EntitySpecificationListContext,0)


        def RPAREN(self):
            return self.getToken(myERParser.RPAREN, 0)

        def attributeBlock(self):
            return self.getTypedRuleContext(myERParser.AttributeBlockContext,0)


        def SEMICOLON(self):
            return self.getToken(myERParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return myERParser.RULE_relationDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationDeclaration" ):
                listener.enterRelationDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationDeclaration" ):
                listener.exitRelationDeclaration(self)




    def relationDeclaration(self):

        localctx = myERParser.RelationDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_relationDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(myERParser.T__4)
            self.state = 65
            self.match(myERParser.Identifier)
            self.state = 66
            self.match(myERParser.LPAREN)
            self.state = 67
            self.entitySpecificationList()
            self.state = 68
            self.match(myERParser.RPAREN)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 69
                self.attributeBlock()


            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 72
                self.match(myERParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationSpecificationListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationSpecification(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(myERParser.RelationSpecificationContext)
            else:
                return self.getTypedRuleContext(myERParser.RelationSpecificationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(myERParser.COMMA)
            else:
                return self.getToken(myERParser.COMMA, i)

        def getRuleIndex(self):
            return myERParser.RULE_relationSpecificationList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationSpecificationList" ):
                listener.enterRelationSpecificationList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationSpecificationList" ):
                listener.exitRelationSpecificationList(self)




    def relationSpecificationList(self):

        localctx = myERParser.RelationSpecificationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_relationSpecificationList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.relationSpecification()
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 76
                self.match(myERParser.COMMA)
                self.state = 77
                self.relationSpecification()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationSpecificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(myERParser.Identifier, 0)

        def multiplicity(self):
            return self.getTypedRuleContext(myERParser.MultiplicityContext,0)


        def primaryKey(self):
            return self.getTypedRuleContext(myERParser.PrimaryKeyContext,0)


        def getRuleIndex(self):
            return myERParser.RULE_relationSpecification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationSpecification" ):
                listener.enterRelationSpecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationSpecification" ):
                listener.exitRelationSpecification(self)




    def relationSpecification(self):

        localctx = myERParser.RelationSpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_relationSpecification)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(myERParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(myERParser.Identifier)
                self.state = 85
                self.multiplicity()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.match(myERParser.Identifier)
                self.state = 87
                self.primaryKey()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myERParser.RULE_multiplicity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicity" ):
                listener.enterMultiplicity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicity" ):
                listener.exitMultiplicity(self)




    def multiplicity(self):

        localctx = myERParser.MultiplicityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_multiplicity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(myERParser.Identifier)
            else:
                return self.getToken(myERParser.Identifier, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(myERParser.COMMA)
            else:
                return self.getToken(myERParser.COMMA, i)

        def getRuleIndex(self):
            return myERParser.RULE_identifierList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierList" ):
                listener.enterIdentifierList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierList" ):
                listener.exitIdentifierList(self)




    def identifierList(self):

        localctx = myERParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_identifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(myERParser.Identifier)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 93
                self.match(myERParser.COMMA)
                self.state = 94
                self.match(myERParser.Identifier)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(myERParser.LBRACKET, 0)

        def dataByte(self):
            return self.getTypedRuleContext(myERParser.DataByteContext,0)


        def RBRACKET(self):
            return self.getToken(myERParser.RBRACKET, 0)

        def getRuleIndex(self):
            return myERParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = myERParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_type)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(myERParser.T__11)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.match(myERParser.T__11)
                self.state = 102
                self.match(myERParser.LBRACKET)
                self.state = 103
                self.dataByte()
                self.state = 104
                self.match(myERParser.RBRACKET)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.match(myERParser.T__12)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 107
                self.match(myERParser.T__12)
                self.state = 108
                self.match(myERParser.LBRACKET)
                self.state = 109
                self.dataByte()
                self.state = 110
                self.match(myERParser.RBRACKET)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 112
                self.match(myERParser.T__13)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 113
                self.match(myERParser.T__14)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 114
                self.match(myERParser.T__15)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 115
                self.match(myERParser.T__15)
                self.state = 116
                self.match(myERParser.LBRACKET)
                self.state = 117
                self.dataByte()
                self.state = 118
                self.match(myERParser.RBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataByteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self):
            return self.getToken(myERParser.Integer, 0)

        def getRuleIndex(self):
            return myERParser.RULE_dataByte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataByte" ):
                listener.enterDataByte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataByte" ):
                listener.exitDataByte(self)




    def dataByte(self):

        localctx = myERParser.DataByteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dataByte)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(myERParser.Integer)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(myERParser.Identifier, 0)

        def primaryKey(self):
            return self.getTypedRuleContext(myERParser.PrimaryKeyContext,0)


        def multiplicity(self):
            return self.getTypedRuleContext(myERParser.MultiplicityContext,0)


        def COLON(self):
            return self.getToken(myERParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(myERParser.TypeContext,0)


        def LBRACE(self):
            return self.getToken(myERParser.LBRACE, 0)

        def attributeDeclarationList(self):
            return self.getTypedRuleContext(myERParser.AttributeDeclarationListContext,0)


        def RBRACE(self):
            return self.getToken(myERParser.RBRACE, 0)

        def getRuleIndex(self):
            return myERParser.RULE_attributeDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeDeclaration" ):
                listener.enterAttributeDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeDeclaration" ):
                listener.exitAttributeDeclaration(self)




    def attributeDeclaration(self):

        localctx = myERParser.AttributeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attributeDeclaration)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(myERParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(myERParser.Identifier)
                self.state = 126
                self.primaryKey()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.match(myERParser.Identifier)
                self.state = 128
                self.multiplicity()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.match(myERParser.Identifier)
                self.state = 130
                self.match(myERParser.COLON)
                self.state = 131
                self.type_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
                self.match(myERParser.Identifier)
                self.state = 133
                self.match(myERParser.COLON)
                self.state = 134
                self.type_()
                self.state = 135
                self.primaryKey()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 137
                self.match(myERParser.Identifier)
                self.state = 138
                self.match(myERParser.COLON)
                self.state = 139
                self.type_()
                self.state = 140
                self.multiplicity()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 142
                self.match(myERParser.Identifier)
                self.state = 143
                self.match(myERParser.LBRACE)
                self.state = 144
                self.attributeDeclarationList()
                self.state = 145
                self.match(myERParser.RBRACE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 147
                self.match(myERParser.Identifier)
                self.state = 148
                self.match(myERParser.LBRACE)
                self.state = 149
                self.attributeDeclarationList()
                self.state = 150
                self.match(myERParser.RBRACE)
                self.state = 151
                self.multiplicity()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeDeclarationListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(myERParser.AttributeDeclarationContext)
            else:
                return self.getTypedRuleContext(myERParser.AttributeDeclarationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(myERParser.COMMA)
            else:
                return self.getToken(myERParser.COMMA, i)

        def getRuleIndex(self):
            return myERParser.RULE_attributeDeclarationList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeDeclarationList" ):
                listener.enterAttributeDeclarationList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeDeclarationList" ):
                listener.exitAttributeDeclarationList(self)




    def attributeDeclarationList(self):

        localctx = myERParser.AttributeDeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_attributeDeclarationList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.attributeDeclaration()
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 156
                self.match(myERParser.COMMA)
                self.state = 157
                self.attributeDeclaration()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntitySpecificationListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entitySpecification(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(myERParser.EntitySpecificationContext)
            else:
                return self.getTypedRuleContext(myERParser.EntitySpecificationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(myERParser.COMMA)
            else:
                return self.getToken(myERParser.COMMA, i)

        def REC(self):
            return self.getToken(myERParser.REC, 0)

        def getRuleIndex(self):
            return myERParser.RULE_entitySpecificationList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntitySpecificationList" ):
                listener.enterEntitySpecificationList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntitySpecificationList" ):
                listener.exitEntitySpecificationList(self)




    def entitySpecificationList(self):

        localctx = myERParser.EntitySpecificationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_entitySpecificationList)
        self._la = 0 # Token type
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.entitySpecification()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==28:
                    self.state = 164
                    self.match(myERParser.COMMA)
                    self.state = 165
                    self.entitySpecification()
                    self.state = 170
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.entitySpecification()
                self.state = 172
                self.match(myERParser.REC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntitySpecificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(myERParser.Identifier, 0)

        def multiplicity(self):
            return self.getTypedRuleContext(myERParser.MultiplicityContext,0)


        def primaryKey(self):
            return self.getTypedRuleContext(myERParser.PrimaryKeyContext,0)


        def getRuleIndex(self):
            return myERParser.RULE_entitySpecification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntitySpecification" ):
                listener.enterEntitySpecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntitySpecification" ):
                listener.exitEntitySpecification(self)




    def entitySpecification(self):

        localctx = myERParser.EntitySpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_entitySpecification)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(myERParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(myERParser.Identifier)
                self.state = 178
                self.multiplicity()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.match(myERParser.Identifier)
                self.state = 180
                self.primaryKey()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryKeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myERParser.RULE_primaryKey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryKey" ):
                listener.enterPrimaryKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryKey" ):
                listener.exitPrimaryKey(self)




    def primaryKey(self):

        localctx = myERParser.PrimaryKeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primaryKey)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






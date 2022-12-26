# Generated from src/grammar/myER.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .myERParser import myERParser
else:
    from myERParser import myERParser

# This class defines a complete listener for a parse tree produced by myERParser.
class myERListener(ParseTreeListener):

    # Enter a parse tree produced by myERParser#program.
    def enterProgram(self, ctx:myERParser.ProgramContext):
        pass

    # Exit a parse tree produced by myERParser#program.
    def exitProgram(self, ctx:myERParser.ProgramContext):
        pass


    # Enter a parse tree produced by myERParser#entityDeclaration.
    def enterEntityDeclaration(self, ctx:myERParser.EntityDeclarationContext):
        pass

    # Exit a parse tree produced by myERParser#entityDeclaration.
    def exitEntityDeclaration(self, ctx:myERParser.EntityDeclarationContext):
        pass


    # Enter a parse tree produced by myERParser#attributeBlock.
    def enterAttributeBlock(self, ctx:myERParser.AttributeBlockContext):
        pass

    # Exit a parse tree produced by myERParser#attributeBlock.
    def exitAttributeBlock(self, ctx:myERParser.AttributeBlockContext):
        pass


    # Enter a parse tree produced by myERParser#relationDeclaration.
    def enterRelationDeclaration(self, ctx:myERParser.RelationDeclarationContext):
        pass

    # Exit a parse tree produced by myERParser#relationDeclaration.
    def exitRelationDeclaration(self, ctx:myERParser.RelationDeclarationContext):
        pass


    # Enter a parse tree produced by myERParser#relationSpecificationList.
    def enterRelationSpecificationList(self, ctx:myERParser.RelationSpecificationListContext):
        pass

    # Exit a parse tree produced by myERParser#relationSpecificationList.
    def exitRelationSpecificationList(self, ctx:myERParser.RelationSpecificationListContext):
        pass


    # Enter a parse tree produced by myERParser#relationSpecification.
    def enterRelationSpecification(self, ctx:myERParser.RelationSpecificationContext):
        pass

    # Exit a parse tree produced by myERParser#relationSpecification.
    def exitRelationSpecification(self, ctx:myERParser.RelationSpecificationContext):
        pass


    # Enter a parse tree produced by myERParser#multiplicity.
    def enterMultiplicity(self, ctx:myERParser.MultiplicityContext):
        pass

    # Exit a parse tree produced by myERParser#multiplicity.
    def exitMultiplicity(self, ctx:myERParser.MultiplicityContext):
        pass


    # Enter a parse tree produced by myERParser#identifierList.
    def enterIdentifierList(self, ctx:myERParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by myERParser#identifierList.
    def exitIdentifierList(self, ctx:myERParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by myERParser#type.
    def enterType(self, ctx:myERParser.TypeContext):
        pass

    # Exit a parse tree produced by myERParser#type.
    def exitType(self, ctx:myERParser.TypeContext):
        pass


    # Enter a parse tree produced by myERParser#dataByte.
    def enterDataByte(self, ctx:myERParser.DataByteContext):
        pass

    # Exit a parse tree produced by myERParser#dataByte.
    def exitDataByte(self, ctx:myERParser.DataByteContext):
        pass


    # Enter a parse tree produced by myERParser#attributeDeclaration.
    def enterAttributeDeclaration(self, ctx:myERParser.AttributeDeclarationContext):
        pass

    # Exit a parse tree produced by myERParser#attributeDeclaration.
    def exitAttributeDeclaration(self, ctx:myERParser.AttributeDeclarationContext):
        pass


    # Enter a parse tree produced by myERParser#attributeDeclarationList.
    def enterAttributeDeclarationList(self, ctx:myERParser.AttributeDeclarationListContext):
        pass

    # Exit a parse tree produced by myERParser#attributeDeclarationList.
    def exitAttributeDeclarationList(self, ctx:myERParser.AttributeDeclarationListContext):
        pass


    # Enter a parse tree produced by myERParser#entitySpecificationList.
    def enterEntitySpecificationList(self, ctx:myERParser.EntitySpecificationListContext):
        pass

    # Exit a parse tree produced by myERParser#entitySpecificationList.
    def exitEntitySpecificationList(self, ctx:myERParser.EntitySpecificationListContext):
        pass


    # Enter a parse tree produced by myERParser#entitySpecification.
    def enterEntitySpecification(self, ctx:myERParser.EntitySpecificationContext):
        pass

    # Exit a parse tree produced by myERParser#entitySpecification.
    def exitEntitySpecification(self, ctx:myERParser.EntitySpecificationContext):
        pass


    # Enter a parse tree produced by myERParser#primaryKey.
    def enterPrimaryKey(self, ctx:myERParser.PrimaryKeyContext):
        pass

    # Exit a parse tree produced by myERParser#primaryKey.
    def exitPrimaryKey(self, ctx:myERParser.PrimaryKeyContext):
        pass



del myERParser
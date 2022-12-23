from ParserER import Node
from Attribute import Attribute

class Entity:
    def __init__(self, node: Node):
        assert node.type == 'entityDeclaration'
        self.attributes = {}
        self.primaryKey = []
        self.relationSpecifications = {}
        self.identifier = node.getChildByType('Identifier').text
        attributeDeclarationNodes = node.getChildByType('attributeBlock').getChildByType('attributeDeclarationList').getChildrenByType('attributeDeclaration')
        
        #   Attributes
        for attributeDeclarationNode in attributeDeclarationNodes:
            identifier = attributeDeclarationNode.getChildByType('Identifier').text
            attribute = Attribute(attributeDeclarationNode)
            self.attributes[identifier] = attribute
            if attribute.isPk():
                self.primaryKey.append(attribute)
        
        #   Relations specifications   
        if node.getChildByType('relationSpecificationList') is not None:
            relationSpecificationNodes = node.getChildByType('relationSpecificationList').getChildrenByType('relationSpecification')
            for relationSpecificationNode in relationSpecificationNodes:
                #print(relationSpecificationNode.getChildByType('Identifier'))
                pass
        
    def getAttributes(self):
        if any(self.attributes):
            return self.attributes
        else:
            return None

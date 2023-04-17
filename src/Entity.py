from ParserER import Node
from Attribute import Attribute

class Entity:
    def __init__(self, node: Node):
        assert node.type == 'entityDeclaration'
        self.attributes = {}
        self.primaryKey = []
        self.relationSpecifications = {}
        #self.generalization = {node.getChildByType('SPECIALIZED BY'),}
        self.identifier = node.getChildByType('Identifier').text
        attributeDeclarationNodes = node.getChildByType('attributeBlock').getChildByType('attributeDeclarationList').getChildrenByType('attributeDeclaration')
        
        #   Attributes
        for attributeDeclarationNode in attributeDeclarationNodes:
            attributeIdentifier = attributeDeclarationNode.getChildByType('Identifier').text
            attribute = Attribute(attributeDeclarationNode)
            self.attributes[attributeIdentifier] = attribute
            if attribute.isPk():
                self.primaryKey.append(attribute)
        
        #   Relation specifications   
        if node.getChildByType('relationSpecificationList') is not None:
            relationSpecificationNodes = node.getChildByType('relationSpecificationList').getChildrenByType('relationSpecification')
            for relationSpecificationNode in relationSpecificationNodes:
                relationIdentifier = relationSpecificationNode.getChildByType('Identifier').text
                specification = Specificatiion(relationSpecificationNode)
                self.relationSpecifications[relationIdentifier] = specification
        
    def getAttributes(self) -> dict:
        if any(self.attributes):
            return self.attributes
        else:
            return None
    
    def getRelationSpecifications(self) -> dict:
        if any(self.relationSpecifications):
            return self.relationSpecifications
        else:
            return None
    
    def getIdentifier(self):
        return self.identifier
    
class Specificatiion:
    def __init__(self, node: Node) -> None:
        self.entityName = node.getChildByType('Identifier').text
        self.isPK = node.getChildByType('primaryKey').text if node.getChildByType('primaryKey') is not None else None
        
    def getEntityName(self):
        return self.entityName
    
    def isPk(self) -> bool:
        if  self.isPK:
            return True
        else:
            return False
from ParserER import Node
from Attribute import Attribute
class Relation:
    def __init__(self, node: Node):
        assert node.type == 'relationDeclaration'
        self.attributes = {}
        self.primaryKey = []
        self.entitySpecifications = {}
        self.recursive = False
        self.identifier = node.getChildByType('Identifier').text
        if node.getChildByType('attributeBlock') is not None:
            attributeDeclarationNodes = node.getChildByType('attributeBlock').getChildByType('attributeDeclarationList').getDescendantsByType('attributeDeclaration')
            for attributeDeclarationNode in attributeDeclarationNodes:
                self.identifier = attributeDeclarationNode.getChildByType('Identifier').text
                attribute = Attribute(attributeDeclarationNode)
                self.attributes[self.identifier] = attribute
                if attribute.isPk():
                    self.primaryKey.append(attribute)
                    
        if node.getChildByType('entitySpecificationList') is not None:
            entitySpecificationNodes = node.getChildByType('entitySpecificationList').getDescendantsByType('entitySpecification')
            for entitySpecificationNode in entitySpecificationNodes:
                isRecursive = node.getChildByType('entitySpecificationList').getChildByType('REC')
                if isRecursive is not None:
                    self.recursive = True
                identifier = entitySpecificationNode.getChildByType('Identifier').text
                specification = Specificatiion(entitySpecificationNode)
                self.entitySpecifications[identifier] = specification
                if specification.isPk():
                    self.primaryKey.append(specification)
        
    def isRecursive(self) -> bool:
        if  self.recursive:
            return True
        else:
            return False
        
    def getAttributes(self):
        return self.attributes
    
    def getPrimarykey(self):
        return self.primaryKey
    
    def getEntitySpecifications(self):
        return self.entitySpecifications
              
class Specificatiion:
    def __init__(self, node: Node) -> None:
        self.entityName = node.getChildByType('Identifier')
        self.isPK = node.getChildByType('primaryKey')
        self.multiplicity = node.getChildByType('multiplicity')
    
    def getEntityName(self):
        return self.entityName
    
    def isPk(self) -> bool:
        if  self.isPK:
            return True
        else:
            return False
    
    def getMultiplicity(self):
        return self.multiplicity
    
    
            
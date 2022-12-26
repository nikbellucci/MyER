from ParserER import Node

class Attribute:
    def __init__(self, node: Node):
        assert node.type == 'attributeDeclaration'
        self.primaryKey = node.getChildByType('primaryKey').text if node.getChildByType('primaryKey') is not None else None
        self.type = node.getChildByType('type') if node.getChildByType('type') is not None else 'CompositeAttribute'
        
        if self.type != 'CompositeAttribute':
            self. dataByte = self.type.getChildByType('dataByte').text if self.type.getChildByType('dataByte') is not None else None
        else:
            self.dataByte = None
        print(self.dataByte)
        
        self.identifier = node.getChildByType('Identifier').text
        self.multiplicity = node.getChildByType('multiplicity').text if node.getChildByType('multiplicity') is not None else None
        if node.getChildByType('attributeDeclarationList') is not None:
            self.subAttributes = {}
            attributeDeclarationNodes = node.getChildByType('attributeDeclarationList').getDescendantsByType('attributeDeclaration')
            for attributeDeclarationNode in attributeDeclarationNodes:
                attributeIdentifier = attributeDeclarationNode.getChildByType('Identifier').text
                attribute = Attribute(attributeDeclarationNode)
                self.subAttributes[attributeIdentifier] = attribute
                
    def isPk(self) -> bool:
        if  self.primaryKey:
            return True
        else:
            return False
        
    def getType(self):
        return self.type
    
    def getSubAttributes(self) -> dict:
        if any(self.subAttributes):
            return self.subAttributes
        else:
            return None
    
    def getIdentifier(self):
        return self.identifier

    def getMultiplicity(self):
        return self.multiplicity
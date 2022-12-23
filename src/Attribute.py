from ParserER import Node

class Attribute:
    def __init__(self, node: Node):
        assert node.type == 'attributeDeclaration'
        self.primaryKey = node.getChildByType('primaryKey')
        self.type = node.getChildByType('type')
        self.identifier = node.getChildByType('Identifier')
        if node.getChildByType('attributeDeclarationList') is not None:
            self.subAttributes = {}
            self.attributeDeclarationNodes = node.getChildByType('attributeDeclarationList').getDescendantsByType('attributeDeclaration')
            for attributeDeclarationNode in self.attributeDeclarationNodes:
                identifier = attributeDeclarationNode.getChildByType('Identifier').text
                attribute = Attribute(attributeDeclarationNode)
                self.subAttributes[identifier] = attribute
                if attribute.isPk():
                    self.primaryKey.append(attribute)
                
    def isPk(self) -> bool:
        if  self.primaryKey:
            return True
        else:
            return False
        
    def getType(self):
        return self.type
    
    def getSubAttributes(self):
        if any(self.subAttributes):
            return self.subAttributes
        else:
            return None
    
    def getIdentifier(self):
        return self.identifier

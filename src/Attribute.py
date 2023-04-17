from ParserER import Node

class Attribute:
    def __init__(self, node: Node):
        assert node.type == 'attributeDeclaration'
        self.primaryKey = node.getChildByType('primaryKey').text if node.getChildByType('primaryKey') is not None else None
        self.type_data_raw = node.getChildByType('type').text if node.getChildByType('type') is not None else 'CompositeAttribute'
        self.dataByte = None
        
        head, sep, tail = self.type_data_raw.partition('[')
        self.type_data = head
        
        if (node.getChildByType('type') is not None):
            if node.getChildByType('type').getChildByType('dataByte') is not None:   
                # print(node.getChildByType('type').getChildByType('dataByte').text)
                self.dataByte = node.getChildByType('type').getChildByType('dataByte').text
                
        self.identifier = node.getChildByType('Identifier').text
        self.multiplicity = node.getChildByType('multiplicity').text if node.getChildByType('multiplicity') is not None else None
        if node.getChildByType('attributeDeclarationList') is not None:
            self.subAttributes = {}
            attributeDeclarationNodes = node.getChildByType('attributeDeclarationList').getDescendantsByType('attributeDeclaration')
            for attributeDeclarationNode in attributeDeclarationNodes:
                attributeIdentifier = attributeDeclarationNode.getChildByType('Identifier').text
                attribute = Attribute(attributeDeclarationNode)
                self.subAttributes[attributeIdentifier] = attribute
                # FIXME Se un attributo non viene specificato con il tipo il parser crasha 
                # TODO Controllo se non esistono subattribute nel caso non creare nessun dizionario
                
    def isPk(self) -> bool:
        if  self.primaryKey:
            return True
        else:
            return False
        
    def getType(self):
        return self.type_data
    
    def getSubAttributes(self) -> dict:
        if any(self.subAttributes):
            return self.subAttributes
        else:
            return None
    
    def getIdentifier(self):
        return self.identifier

    def getMultiplicity(self):
        return self.multiplicity
    
    def getDataByte(self):
        return self.dataByte
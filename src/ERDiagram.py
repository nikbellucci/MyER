from Parser import Node

class Attribute:
    def __init__(self, node: Node):
        assert node.type == 'attributeDeclaration'
        # self.isPk = 
        pass
    
    def isPk(self) -> bool:
        pass

class Relation:
    pass

class Entity:
    def __init__(self, node: Node):
        assert node.type == 'entityDeclaration'
        self.attributes = {}
        self.primaryKey = []
        self.identifier = node.getChildByType('Identifier').text
        attributeDeclarationNodes = node.getChildByType('attributeBlock').getChildByType('attributeDeclarationList').getChildrenByType('attributeDeclaration')
        for attributeDeclarationNode in attributeDeclarationNodes:
            identifier = attributeDeclarationNode.getChildByType('Identifier').text
            attribute = Attribute(attributeDeclarationNode)
            self.attributes[identifier] = attribute
            if attribute.isPk():
                self.primaryKey.append(attribute)
        
        if node.getChildByType('relationSpecificationList') is not None:
            relationSpecificationNodes = node.getChildByType('relationSpecificationList').getChildrenByType('relationSpecification')
            for relationSpecificationNode in relationSpecificationNodes:
                pass
        pass




class ERDiagram:
    def __init__(self, tree):
        self.entities = {}
        self.relations = {}
        self.__build(tree)

    def __build(self, tree: Node):
        for declarationNode in tree.children:
            identifier = declarationNode.getChildByType('Identifier').text
            if declarationNode.type == 'entityDeclaration':
                self.entities[identifier] = Entity(declarationNode)
            elif declarationNode.type == 'relationDeclaration':
                self.relations[identifier] = Relation(declarationNode)
    




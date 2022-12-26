from ParserER import Node
from Entity import Entity
from Relation import Relation
class ERDiagram:
    def __init__(self, tree):
        self.entities = {}
        self.relations = {}
        self.__build(tree)
        
    #Esempio di come accedere alle proprietà di un attributo
    #test = self.entities.get('SalaTe').attributes['Foto'].primaryKey
    
    #Esempio di come accedere alle proprietà di una relazione
    #print(self.relations.get('Adiacenza').isRecursive())

    def __build(self, tree: Node):
        for declarationNode in tree.children:
            identifier = declarationNode.getChildByType('Identifier').text
            if declarationNode.type == 'entityDeclaration':
                self.entities[identifier] = Entity(declarationNode)
            elif declarationNode.type == 'relationDeclaration':
                self.relations[identifier] = Relation(declarationNode)
        
        #for entityIdentifier in self.entities.keys():
        #    print('-----------------------------')
        #    print('Entità:', entityIdentifier)
        #    for attributeIdentifier in self.entities.get(entityIdentifier).getAttributes().keys():
        #        print('Attributo: ', attributeIdentifier, self.entities.get(entityIdentifier).getAttributes().get(attributeIdentifier).getType())
        #    print('-----------------------------')
        #subAttributess = self.entities.get('PuntoVendita').getAttributes().get('Indirizzo').getSubAttributes()
        #print(subAttributess.get('Via').getIdentifier())
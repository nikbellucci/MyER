from ParserER import Node
from Entity import Entity
from Relation import Relation
from Graph import Node
from Graph import Graph
class ERDiagram:
    def __init__(self, tree):
        self.entities = {}
        self.relations = {}
        self.entity_graph = Graph()
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
        
        # --------------
        # for entityIdentifier in self.entities.keys():
        #    print('-----------------------------')
        #    print('Entità:', entityIdentifier)
        #    for attributeIdentifier in self.entities.get(entityIdentifier).getAttributes().keys():
        #     #    print(self.entities.get(entityIdentifier).getAttributes().keys())
        #        print('Attributo:', attributeIdentifier,'->', self.entities.get(entityIdentifier).getAttributes().get(attributeIdentifier).getType())
        #        if self.entities.get(entityIdentifier).getAttributes().get(attributeIdentifier).getType() == 'CompositeAttribute':
        #            for subAttributes in self.entities.get(entityIdentifier).getAttributes().get(attributeIdentifier).getSubAttributes():
        #                print('---Attributo composito:', subAttributes,'->', self.entities.get(entityIdentifier).getAttributes().get(attributeIdentifier).getSubAttributes().get(subAttributes).getType())
        #    print('-----------------------------')
        # subAttributes = self.entities.get('PuntoVendita').getAttributes().get('Indirizzo').getSubAttributes()
        # print(subAttributes.get('Via').getIdentifier())
        
        for entityIdentifier in self.entities.keys():
            # print(self.entities.get(entityIdentifier).getIdentifier())
            node = Node(self.entities.get(entityIdentifier))
            # print(node)
            # for attributeIdentifier in self.entities.get(entityIdentifier).getAttributes():
            #     name_attribute = attributeIdentifier
            #     type_attribute = self.entities.get(entityIdentifier).getAttributes().get(attributeIdentifier).getType()
            #     # print(name_attribute, type_attribute)
            #     node = Node(entityIdentifier, (name_attribute, type_attribute))
            #     print(node.attributes)
                # self.entity_graph.add_node(node)
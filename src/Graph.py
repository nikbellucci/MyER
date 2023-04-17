class Graph:
    def __init__(self) -> None:
        self.nodes = []
        
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
    
    def add_edge(self, first_node, second_node):
        # first_node.adjacent
        pass    
        
class Node:
    def __init__(self, entity) -> None:
        
        self.name = entity.getIdentifier()
        self.attributes = {}
        self.sub_attributes = {}
        
        for attributeIdentifier in entity.getAttributes():
                name_attribute = attributeIdentifier
                type_attribute = entity.getAttributes().get(attributeIdentifier).getType()
                data_byte = entity.getAttributes().get(attributeIdentifier).getDataByte()
                is_primary_key = entity.getAttributes().get(attributeIdentifier).isPk()
                if type_attribute == 'CompositeAttribute':
                    for subAttributeIdentfier in entity.getAttributes().get(name_attribute).getSubAttributes():
                        self.sub_attributes[subAttributeIdentfier] = entity.getAttributes().get(name_attribute).getSubAttributes().get(subAttributeIdentfier)
                        # print(self.sub_attributes)
                        # TODO salvare i dati dei subattribute non formattati
                    add_values_in_dict(self.attributes, name_attribute,[type_attribute, data_byte, is_primary_key, self.sub_attributes])
                # print(type_attribute)
                # TODO i subattribute non vengono salvati
                add_values_in_dict(self.attributes, name_attribute,[type_attribute, data_byte, is_primary_key])
                print(self.attributes)
                
        # self.generalizations = generalizations
        self.adjacent = []
        
    def add_adjacent(self, node):
        if node not in self.adjacent:
            self.adjacent.append(node)
            
            
def add_values_in_dict(sample_dict, key, list_of_values):
    
    if key not in sample_dict:
        sample_dict[key] = list()
        
    sample_dict[key].extend(list_of_values)
    
    return sample_dict

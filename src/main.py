import sys
from ParserER import ParserER
from ERDiagram import ERDiagram
from pathlib import Path

if __name__ == '__main__':
    # example = Path("../examples/Test.er")
    # tree = ParserER.buildParseTree(example)
    tree = ParserER.buildParseTree(sys.argv[1])
    
    erDiagram = ERDiagram(tree)
    
    # print(erDiagram.entities.get('PuntoVendita').getAttributes().get('Indirizzo').getSubAttributes().get('Cap').getType())
    # print(erDiagram.entities.get('PuntoVendita').getAttributes().get('Indirizzo').getSubAttributes().get('Cap'))

    # for entity in erDiagram.getEntities():
        # drawRectangle(entity.identifier)
        # for attribute in entity.getAttributes():
            # drawLineWithDot(attribute.identifier, filled=attribute.isPk())

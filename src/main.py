import sys
from ParserER import ParserER
from ERDiagram import ERDiagram

if __name__ == '__main__':
    tree = ParserER.buildParseTree(sys.argv[1])
    # tree = ParserER.buildParseTree('/workspaces/MyER/examples/PuntoVendita.er')
    erDiagram = ERDiagram(tree)
    #print(erDiagram.entities.get('PuntoVendita').getAttributes().get('Indirizzo').getSubAttributes().get('Via'))
    #for entity in erDiagram.entities:
    #    print(entity, 'attributi:',)

    # for entity in erDiagram.getEntities():
        # drawRectangle(entity.identifier)
        # for attribute in entity.getAttributes():
            # drawLineWithDot(attribute.identifier, filled=attribute.isPk())

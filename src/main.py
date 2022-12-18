import sys
from Parser import Parser
from ERDiagram import ERDiagram

if __name__ == '__main__':
    tree = Parser.buildParseTree(sys.argv[1])
    erDiagram = ERDiagram(tree)


    # for entity in erDiagram.getEntities():
        # drawRectangle(entity.identifier)
        # for attribute in entity.getAttributes():
            # drawLineWithDot(attribute.identifier, filled=attribute.isPk())


    



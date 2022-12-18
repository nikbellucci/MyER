grammar myER;

/****** Parser grammar ******/
program
    : (entityDeclaration | relationDeclaration)*;

entityDeclaration
    : 'ENTITY' Identifier (LPAREN relationSpecificationList? RPAREN)? 
    (('EXTENDS' | 'SPECIALIZES') identifierList)?
    attributeBlock? ('SPECIALIZED BY' identifierList)? SEMICOLON?;

attributeBlock
    : LBRACE attributeDeclarationList RBRACE;

relationDeclaration
    : 'RELATION' Identifier LPAREN entitySpecificationList RPAREN attributeBlock? SEMICOLON?;

relationSpecificationList
    : relationSpecification (COMMA relationSpecification)*;

relationSpecification
    : Identifier
    | Identifier multiplicity
    | Identifier primaryKey
    ;

multiplicity
    : '[0-1]'
    | '[1-1]'
    | '[1-N]'
    | '[1-n]'
    | '[0-N]'
    | '[0-n]'
    ;

identifierList
    : Identifier (COMMA Identifier)*;

type
    : 'string'
    | 'string' LBRACKET Integer RBRACKET
    | 'integer'
    | 'boolean'
    | 'date'
    | 'float'
    ;

attributeDeclaration
    : Identifier
    | Identifier primaryKey
    | Identifier multiplicity
    | Identifier COLON type
	| Identifier COLON type primaryKey
	| Identifier COLON type multiplicity
    | Identifier LBRACE attributeDeclarationList RBRACE
	| Identifier LBRACE attributeDeclarationList RBRACE multiplicity
    ;

attributeDeclarationList
    : attributeDeclaration (COMMA attributeDeclaration)*;

entitySpecificationList
    : entitySpecification (COMMA entitySpecification)*
	| entitySpecification REC
    ;

entitySpecification
    : Identifier
    | Identifier multiplicity
    | Identifier primaryKey
    ;

primaryKey
    : 'PK'
    | 'PRIMARY KEY'
    ;

/***** Lexer grammar ****/

LBRACKET: '[';
RBRACKET: ']';

LBRACE: '{';
RBRACE: '}';

LPAREN: '(';
RPAREN: ')';

COLON: ':';
SEMICOLON: ';';

DOT: '.';
COMMA: ',';

DASH: '-';
REC: '*';


Whitespace: [ \t]+ -> skip;
Newline: [\r\n]+ -> skip;

fragment Digit: [0-9];
Integer: Digit+;

fragment UpperCaseLetter: [A-Z];
fragment LowerCaseLetter: [a-z];
fragment Letter: LowerCaseLetter | UpperCaseLetter;
fragment FirstIdCharacter: Letter;
fragment GeneralIdCharacter: FirstIdCharacter | Integer | '_';

Identifier: FirstIdCharacter GeneralIdCharacter*;

LineComment: '//' ~[\r\n]* -> skip;
BlockComment: '/*' .*? '*/' -> skip;
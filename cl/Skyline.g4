grammar Skyline;

root : (assign|expr) EOF ;

assign: ID ':=' expr;

expr: '(' expr ')' #parentesisExp
| sky #skyExp
| '-' expr #reflectExp
| expr '*' expr #interExp
| expr '*' NUM #multExp
| expr '+' expr #unionExp
| expr '+' NUM #rightExp
| expr '-' NUM #leftExp
;

sky: ID | crea ;
crea: '(' ( NUM (',' NUM)* )? ')';

NUM : (DIGIT)+ ;
DIGIT : '0'..'9';
ID : LETTER (LETTER|DIGIT)*;
LETTER : ('A'..'Z'|'a'..'z');
WS : [ \n]+ -> skip ;

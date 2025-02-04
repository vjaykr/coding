%{
/* Header Section */
#include <stdio.h>
%}

%%

[0-9]+              { printf("TOKEN: NUMBER -> %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]* { printf("TOKEN: IDENTIFIER -> %s\n", yytext); }
"+"                 { printf("TOKEN: PLUS\n"); }
"="                 { printf("TOKEN: EQUAL\n"); }
[ \t\n]             { /* Ignore whitespace */ }
.                   { printf("TOKEN: UNKNOWN -> %s\n", yytext); }

%%

int main() {
    yylex(); /* Call lexical analyzer */
    return 0;
}

int yywrap() {
    return 1; /* End of input */
}

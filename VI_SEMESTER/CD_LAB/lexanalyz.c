%{
#include <stdio.h>
%}

%%
int    { printf("Keyword: int\n"); }
float  { printf("Keyword: float\n"); }
[a-zA-Z_][a-zA-Z0-9_]*  { printf("Identifier: %s\n", yytext); }
[0-9]+  { printf("Number: %s\n", yytext); }
.      { /* Ignore other characters */ }
%%

int main() {
    yylex();
    return 0;
}

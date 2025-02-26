%{
#include <stdio.h>
#include <stdlib.h>
%}

%%

[0-9]+   { printf("Number: %s\n", yytext); }  /* Match one or more digits and print them */
.|\n     { /* Ignore any other characters, including newlines */ }

%%

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    FILE *file = fopen(argv[1], "r");
    if (file == NULL) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }
    yyin = file;
    yylex();
    fclose(file);
    return 0;
}

int yywrap() {
    return 1;
}

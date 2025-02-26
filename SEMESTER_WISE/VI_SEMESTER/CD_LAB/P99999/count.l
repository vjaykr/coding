%{
#include <stdio.h>
#include <stdlib.h>
int line_count = 1;
%}

%%

.*\n    { 
            /* For lines that end with a newline */
            printf("%d: %s", line_count++, yytext);
        }
.+      {
            /* For a final line that may not end with a newline */
            printf("%d: %s\n", line_count++, yytext);
        }

%%

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    
    FILE *file = fopen(argv[1], "r");
    if (!file) {
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

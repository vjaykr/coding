%{
#include <stdio.h>
#include <stdlib.h>

int char_count = 0, word_count = 0, line_count = 0;
%}

%%

\n          { line_count++; char_count++; }      /* Newline: count as line and char */
[ \t]+      { char_count += yyleng; }              /* Whitespace: count chars but no word */
[^ \t\n]+   { word_count++; char_count += yyleng; }  /* Non-whitespace: count as word and chars */

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

    printf("File: %s\n", argv[1]);
    printf("Lines: %d\n", line_count);
    printf("Words: %d\n", word_count);
    printf("Characters: %d\n", char_count);
    return 0;
}

int yywrap() {
    return 1;
}

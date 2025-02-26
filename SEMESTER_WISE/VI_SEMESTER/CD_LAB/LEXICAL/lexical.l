%{
#include <stdio.h>

// Global counters
int char_count = 0, word_count = 0, line_count = 0;
%}

%%
// Rule for counting new lines
\n         { line_count++; char_count++; }

// Rule for counting words (any non-whitespace sequence)
[^\n\s]+   { word_count++; char_count += yyleng; }

// Rule for counting other characters
.          { char_count++; }

%%

// Function required by Flex to indicate the end of file
int yywrap() {
    return 1;
}

// Main function
int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        printf("Error: Cannot open file %s\n", argv[1]);
        return 1;
    }

    yyin = file;
    yylex();  // Start lexical analysis

    // Print results
    printf("File: %s\n", argv[1]);
    printf("Number of Characters: %d\n", char_count);
    printf("Number of Words: %d\n", word_count);
    printf("Number of Lines: %d\n", line_count);

    fclose(file);
    return 0;
}

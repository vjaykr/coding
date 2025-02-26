%{
#include <stdio.h>
#include <stdlib.h>

int vowel_count = 0;
int consonant_count = 0;
%}

%%

[AaEeIiOoUu]    { vowel_count++; }  /* Count vowels */
[a-zA-Z]        { consonant_count++; }  /* Count any letter as consonant if not a vowel */
.               { /* Ignore any other character */ }

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
    printf("Vowels: %d\n", vowel_count);
    printf("Consonants: %d\n", consonant_count);
    return 0;
}

int yywrap() {
    return 1;
}

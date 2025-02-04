#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    int length;
    int vowels = 0, consonants = 0, digits = 0, symbols = 0;







    printf("Enter The string: ");
    gets(str);

    length = strlen(str);

    for (int i = 0; i < length; i++) {
        if ((str[i] >= 'a' && str[i] <= 'z') || (str[i] >= 'A' && str[i] <= 'Z')) {
            if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u' ||
                str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U') {
                vowels++;
            } else {
                consonants++;
            }
        } else if (str[i] >= '0' && str[i] <= '9') {
            digits++;
        } else if (str[i] != ' ') {
            symbols++;
        }
    }

    printf("Vowels: %d\n", vowels);
    printf("Consonants: %d\n", consonants);
    printf("Digits: %d\n", digits);
    printf("Symbols: %d\n", symbols);
}
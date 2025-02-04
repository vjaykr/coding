#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str1[50] = "Hello";
    char str2[50] = "World";
    char str3[50];
    char str4[50];
    char str5[50] = "Hello World";
    char *ptr;

    // strlen
    printf("Length of str1: %zu\n", strlen(str1));

    // strlwr
    strcpy(str3, str1);
    for(int i = 0; str3[i]; i++) {
        str3[i] = tolower(str3[i]);
    }
    printf("Lowercase str1: %s\n", str3);

    // strupr
    strcpy(str4, str1);
    for(int i = 0; str4[i]; i++) {
        str4[i] = toupper(str4[i]);
    }
    printf("Uppercase str1: %s\n", str4);

    // strcat
    strcat(str1, str2);
    printf("Concatenated str1 and str2: %s\n", str1);

    // strncat  
    strncat(str1, str2, 3);
    printf("Concatenated first 3 characters of str2 to str1: %s\n", str1);

    // strcpy
    strcpy(str3, str2);
    printf("Copied str2 to str3: %s\n", str3);

    // strncpy
    strncpy(str4, str2, 3);
    str4[3] = '\0';
    printf("Copied first 3 characters of str2 to str4: %s\n", str4);

    // strcmp
    printf("Comparison of str1 and str2: %d\n", strcmp(str1, str2));

    // strncmp
    printf("Comparison of first 3 characters of str1 and str2: %d\n", strncmp(str1, str2, 3));

    // strcmpi (stricmp)
    printf("Case insensitive comparison of str1 and str2: %d\n", strcasecmp(str1, str2));

    // strdup
    char *str6 = strdup(str5);
    printf("Duplicated str5: %s\n", str6);
    free(str6);

    // strchr
    ptr = strchr(str5, 'o');
    if(ptr) {
        printf("First occurrence of 'o' in str5: %s\n", ptr);
    }

    // strrchr
    ptr = strrchr(str5, 'o');
    if(ptr) {
        printf("Last occurrence of 'o' in str5: %s\n", ptr);
    }

    // strstr
    ptr = strstr(str5, "World");
    if(ptr) {
        printf("Substring 'World' in str5: %s\n", ptr);
    }

    // strset (not standard in C, using memset instead)
    memset(str5, '*', 5);
    printf("Set first 5 characters of str5 to '*': %s\n", str5);

    // strnset (not standard in C, using custom implementation)
    strncpy(str5, "Hello World", 11);
    for(int i = 0; i < 5; i++) {
        str5[i] = '*';
    }
    printf("Set first 5 characters of str5 to '*': %s\n", str5);

    // strrev (not standard in C, using custom implementation)
    int len = strlen(str5);
    for(int i = 0; i < len / 2; i++) {
        char temp = str5[i];
        str5[i] = str5[len - i - 1];
        str5[len - i - 1] = temp;
    }
    printf("Reversed str5: %s\n", str5);

    return 0;
}
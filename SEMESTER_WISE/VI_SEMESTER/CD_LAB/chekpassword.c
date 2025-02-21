#include <stdio.h>
#include <string.h>
#include <conio.h>

#define USERNAME "chitranjan"
#define PASSWORD "securepassword"

int main() {
    char username[50], input_password[50];
    int i = 0, j = 0;
    char ch;

    // Prompt for username
    printf("Enter username: ");
    fgets(username, 50, stdin);
    // Remove newline character at the end of input if present
    username[strcspn(username, "\n")] = '\0';

    // Prompt for password
    printf("Enter password: ");
    
    while ((ch = getch()) != '\r' && i < 49) { // '\r' is the Enter key
        if (ch == '\b') { // Handle backspace
            if (i > 0) {
                printf("\b \b");
                i--;
            }
        } else {
            input_password[i++] = ch;
            printf("*");
        }
    }
    input_password[i] = '\0'; // Null-terminate the password string

    printf("\n");

    // Check if both username and password are correct
    if (strcmp(username, USERNAME) == 0 && strcmp(input_password, PASSWORD) == 0) {
        printf("Login successful.\n");
    } else {
        printf("Invalid username or password.\n");
    }

    return 0;
}

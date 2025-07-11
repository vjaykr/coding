#include <stdio.h> 
 
int main() { 
    char message[100]; 
    int key, i, choice; 
 
    printf("Enter a message (letters and spaces only): "); 
    scanf(" %[^\n]", message);  // Read full line including spaces 
 
    printf("Enter key (number of positions to shift): "); 
    scanf("%d", &key); 
 
    printf("Choose:\n1. Encrypt\n2. Decrypt\nEnter your choice: "); 
    scanf("%d", &choice); 
 
    for (i = 0; message[i] != '\0'; i++) { 
        char ch = message[i]; 
 
        if (ch >= 'A' && ch <= 'Z') { 
            if (choice == 1) 
                message[i] = ((ch - 'A' + key) % 26) + 'A'; 
            else if (choice == 2) 
                message[i] = ((ch - 'A' - key + 26) % 26) + 'A'; 
        } else if (ch >= 'a' && ch <= 'z') { 
            if (choice == 1) 
                message[i] = ((ch - 'a' + key) % 26) + 'a'; 
            else if (choice == 2) 
                message[i] = ((ch - 'a' - key + 26) % 26) + 'a'; 
        } 
        // If it's a space or any other character, we leave it unchanged 
    } 
 
    if (choice == 1) 
        printf("Encrypted message: %s\n", message); 
    else if (choice == 2) 
        printf("Decrypted message: %s\n", message); 
    else 
        printf("Invalid choice!\n"); 
return 0; 
}
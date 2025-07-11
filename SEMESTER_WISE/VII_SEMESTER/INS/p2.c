#include <stdio.h> 
#include <string.h> 
 
void encrypt(char message[], char key[]) { 
    for (int i = 0; message[i] != '\0'; i++) { 
        char ch = message[i]; 
 
        if (ch >= 'A' && ch <= 'Z') { 
            // Uppercase encryption 
            message[i] = key[ch - 'A']; 
        } else if (ch >= 'a' && ch <= 'z') { 
            // Lowercase encryption (convert using same key) 
            message[i] = key[ch - 'a'] + 32; 
        } 
        // spaces and other characters are left unchanged 
    } 
} 
 
void decrypt(char message[], char key[]) { 
    char reverseKey[26]; 
    // Create reverse mapping for uppercase 
    for (int i = 0; i < 26; i++) { 
        reverseKey[key[i] - 'A'] = 'A' + i; 
    } 
 
    for (int i = 0; message[i] != '\0'; i++) { 
        char ch = message[i]; 
 
        if (ch >= 'A' && ch <= 'Z') { 
            // Uppercase decryption 
            message[i] = reverseKey[ch - 'A']; 
        } else if (ch >= 'a' && ch <= 'z') { 
            // Lowercase decryption (convert using reverse key) 
            message[i] = reverseKey[ch - 'a'] + 32; 
        } 
        // spaces and other characters are left unchanged 
    } 
} 
 
int main() { 
    char message[100]; 
    // Fixed substitution key (must be permutation of A-Z) 
    char key[26] = {'Q','W','E','R','T','Y','U','I','O','P', 
                    'A','S','D','F','G','H','J','K','L','Z', 
                    'X','C','V','B','N','M'}; 
    int choice; 
 
    printf("Enter the message: "); 
    scanf(" %[^\n]", message);  // Accept spaces in input 
 
    printf("Choose:\n1. Encrypt\n2. Decrypt\nEnter your choice: "); 
    scanf("%d", &choice); 
 
    if (choice == 1) { 
        encrypt(message, key); 
        printf("Encrypted message: %s\n", message); 
    } else if (choice == 2) { 
        decrypt(message, key); 
        printf("Decrypted message: %s\n", message); 
    } else { 
        printf("Invalid choice!\n"); 
    } 
    return 0; 
}
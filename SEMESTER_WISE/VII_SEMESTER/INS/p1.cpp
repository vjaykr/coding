// Program to convert plain text to Caesar cipher

#include <bits/stdc++.h> // Includes all standard C++ libraries
using namespace std; // Use the standard namespace

// Function to perform Caesar cipher encryption
string ceaserCipher(string text, int key) {
    string result = ""; // Initialize an empty string to store the result

    // Loop through each character in the input text
    for (char c : text) {
        if (isalpha(c)) { // Check if the character is an alphabet letter
            char base = islower(c) ? 'a' : 'A'; // Determine base ('a' for lowercase, 'A' for uppercase)
            // Shift the character by 'key' positions and wrap around using modulo 26
            result += char(int(base + (c - base + key) % 26));
        } else {
            result += c; // Non-alphabetic characters remain unchanged
        }
    }
    return result; // Return the encrypted string
}

int main() {
    string text; // Variable to store the input text
    int key;     // Variable to store the shift value

    cout << "Enter the text to be encrypted: "; // Prompt user for input text
    getline(cin, text); // Read the entire line of text from user

    cout << "Enter the key (shift value): "; // Prompt user for key
    cin >> key; // Read the key value

    key = key % 26; // Ensure the key is within 0-25 (since there are 26 letters)

    string encryptedText = ceaserCipher(text, key); // Encrypt the text using Caesar cipher

    cout << "Encrypted text: " << encryptedText << endl; // Output the encrypted text

    return 0; // Indicate successful program termination
}


//program to convert ciper text to plain text
#include <bits/stdc++.h> // Includes all standard C++ libraries 
using namespace std; // Use the standard namespace
// Function to perform Caesar cipher decryption
string ceaserDecipher(string text, int key) {
    string result = ""; // Initialize an empty string to store the result

    // Loop through each character in the input text
    for (char c : text) {
        if (isalpha(c)) { // Check if the character is an alphabet letter
            char base = islower(c) ? 'a' : 'A'; // Determine base ('a' for lowercase, 'A' for uppercase)
            // Shift the character back by 'key' positions and wrap around using modulo 26
            result += char(int(base + (c - base - key + 26) % 26));
        } else {
            result += c; // Non-alphabetic characters remain unchanged
        }
    }
    return result; // Return the decrypted string
}
int main() {
    string text; // Variable to store the input text
    int key;     // Variable to store the shift value

    cout << "Enter the text to be decrypted: "; // Prompt user for input text
    getline(cin, text); // Read the entire line of text from user

    cout << "Enter the key (shift value): "; // Prompt user for key
    cin >> key; // Read the key value

    key = key % 26; // Ensure the key is within 0-25 (since there are 26 letters)

    string decryptedText = ceaserDecipher(text, key); // Decrypt the text using Caesar cipher

    cout << "Decrypted text: " << decryptedText << endl; // Output the decrypted text

    return 0; // Indicate successful program termination
}

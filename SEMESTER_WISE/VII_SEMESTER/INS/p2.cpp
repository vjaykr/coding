#include <iostream>
#include <string>
using namespace std;

// Caesar Cipher Encryption
string caesarEncrypt(const string& text, int shift) {
    string result = "";
    for (char c : text) {
        if (isupper(c))
            result += char(int('A') + (int(c) - int('A') + shift) % 26);
        else if (islower(c))
            result += char(int('a') + (int(c) - int('a') + shift) % 26);
        else
            result += c;
    }
    return result;
}

// Caesar Cipher Decryption
string caesarDecrypt(const string& text, int shift) {
    return caesarEncrypt(text, 26 - (shift % 26));
}

// Monoalphabetic Cipher Encryption
string monoEncrypt(const string& text, const string& key) {
    string result = "";
    for (char c : text) {
        if (isupper(c))
            result += toupper(key[c - 'A']);
        else if (islower(c))
            result += tolower(key[c - 'a']);
        else
            result += c;
    }
    return result;
}

// Monoalphabetic Cipher Decryption
string monoDecrypt(const string& text, const string& key) {
    string result = "";
    string revKey(26, ' ');
    // Build reverse key
    for (int i = 0; i < 26; ++i) {
        revKey[toupper(key[i]) - 'A'] = char('A' + i);
    }
    for (char c : text) {
        if (isupper(c))
            result += revKey[c - 'A'];
        else if (islower(c))
            result += tolower(revKey[toupper(c) - 'A']);
        else
            result += c;
    }
    return result;
}

int main() {
    string text, key;
    int shift, choice;
    cout << "1. Caesar Cipher\n2. Monoalphabetic Cipher\nChoose: ";
    cin >> choice;
    cin.ignore();
    cout << "Enter text: ";
    getline(cin, text);

    if (choice == 1) {
        cout << "Enter shift: ";
        cin >> shift;
        string enc = caesarEncrypt(text, shift);
        cout << "Encrypted: " << enc << endl;
        cout << "Decrypted: " << caesarDecrypt(enc, shift) << endl;
    } else if (choice == 2) {
        cout << "Enter 26-letter key (e.g., QWERTYUIOPASDFGHJKLZXCVBNM): ";
        cin >> key;
        if (key.length() != 26) {
            cout << "Invalid key length!" << endl;
            return 1;
        }
        string enc = monoEncrypt(text, key);
        cout << "Encrypted: " << enc << endl;
        cout << "Decrypted: " << monoDecrypt(enc, key) << endl;
    } else {
        cout << "Invalid choice." << endl;
    }
    return 0;
}
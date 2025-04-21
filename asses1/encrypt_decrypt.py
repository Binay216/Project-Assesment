import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def encrypt_char(char, n, m):
    if 'a' <= char <= 'z':
        if char <= 'm':
            return chr((ord(char) - ord('a') + n * m) % 26 + ord('a')), 'lm'
        else:
            return chr((ord(char) - ord('a') - (n + m)) % 26 + ord('a')), 'nz'
    elif 'A' <= char <= 'Z':
        if char <= 'M':
            return chr((ord(char) - ord('A') - n) % 26 + ord('A')), 'AM'
        else:
            return chr((ord(char) - ord('A') + m * m) % 26 + ord('A')), 'NZ'
    else:
        return char, 'sp'

def decrypt_char(char, tag, n, m):
    if tag == 'lm':
        return chr((ord(char) - ord('a') - n * m) % 26 + ord('a'))
    elif tag == 'nz':
        return chr((ord(char) - ord('a') + (n + m)) % 26 + ord('a'))
    elif tag == 'AM':
        return chr((ord(char) - ord('A') + n) % 26 + ord('A'))
    elif tag == 'NZ':
        return chr((ord(char) - ord('A') - m * m) % 26 + ord('A'))
    else:
        return char

def encrypt_text(text, n, m):
    encrypted = []
    tags = []
    for c in text:
        enc, tag = encrypt_char(c, n, m)
        encrypted.append(enc)
        tags.append(tag)
    return ''.join(encrypted), tags

def decrypt_text(encrypted_text, tags, n, m):
    decrypted = []
    for c, tag in zip(encrypted_text, tags):
        decrypted.append(decrypt_char(c, tag, n, m))
    return ''.join(decrypted)

def validate(original, decrypted):
    return original.strip() == decrypted.strip()

def main():
    print("Looking in:", os.getcwd())
    n = int(input("Enter value for n: "))
    m = int(input("Enter value for m: "))

    with open("raw_text.txt", "r") as f:
        original_text = f.read()

    encrypted_text, tags = encrypt_text(original_text, n, m)
    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted_text)

    decrypted_text = decrypt_text(encrypted_text, tags, n, m)

    print("\nOriginal:", original_text)
    print("Decrypted:", decrypted_text)

    print("\n--- RESULTS ---")
    print("Encrypted text saved to 'encrypted_text.txt'")
    print("Decryption Validated:", validate(original_text, decrypted_text))

if __name__ == "__main__":
    main()

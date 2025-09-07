def xor_encrypt_decrypt(text, key):
    """
    Encrypts or decrypts a text string using a given key with XOR operation.

    Parameters:
    - text (str): The text to encrypt or decrypt.
    - key (str): The key to use for encryption or decryption.

    Returns:
    - str: The resulting encrypted or decrypted text.
    """
    # Repeat the key to match the length of the text
    extended_key = (key * (len(text) // len(key) + 1))[:len(text)]
    
    # Perform XOR operation between each character of the text and the key
    result = ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(text, extended_key))
    
    return result

# Example usage
key = "secretkey"
plaintext = "Hello from the other side  "

# Encrypt the plaintext
encrypted_text = xor_encrypt_decrypt(plaintext, key)
print(f"Encrypted: {encrypted_text}")

# Decrypt the text
decrypted_text = xor_encrypt_decrypt(encrypted_text, key)
print(f"Decrypted: {decrypted_text}")
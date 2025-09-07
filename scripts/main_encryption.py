# main.py

from bit_manipulation_encryption import xor_encrypt_decrypt
from color_channel_encryption import encode_text_to_image, decode_text_from_image
from hex_edit_encryption import text_to_hex, hex_to_text

def main():
    # User-defined key for XOR encryption
    key = "secretkey"
    
    # Original text to encrypt
    original_text = "Hello, this is a test string!"
    
    # Step 1: Encrypt the text using XOR encryption
    encrypted_text = xor_encrypt_decrypt(original_text, key)
    print(f"Encrypted Text: {encrypted_text}")

    # Step 2: Convert the encrypted text to hexadecimal
    hex_representation = text_to_hex(encrypted_text)
    print(f"Hexadecimal Representation: {hex_representation}")

    # Step 3: Encode the hexadecimal string into the RGB channels of an image
    input_image_path = 'input_image.png'  # Replace with your input image path
    encoded_image_path = 'encoded_image.png'
    encode_text_to_image(input_image_path, encoded_image_path, hex_representation)
    print(f"Encoded image saved as: {encoded_image_path}")

    # Step 4: Decode the text from the image
    decoded_hex = decode_text_from_image(encoded_image_path)
    print(f"Decoded Hexadecimal: {decoded_hex}")

    # Step 5: Convert the hexadecimal back to the original encrypted text
    decrypted_text = hex_to_text(decoded_hex)
    print(f"Decrypted Text: {decrypted_text}")

    # Step 6: Decrypt the text using XOR to get the original text back
    original_decrypted_text = xor_encrypt_decrypt(decrypted_text, key)
    print(f"Original Decrypted Text: {original_decrypted_text}")

if __name__ == "__main__":
    main()
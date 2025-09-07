def text_to_hex(text):
    """
    Converts a text string to its hexadecimal representation.

    Parameters:
    - text (str): The text to convert.

    Returns:
    - str: The hexadecimal representation of the text.
    """
    hex_result = text.encode('utf-8').hex()
    return hex_result

def hex_to_text(hex_string):
    """
    Converts a hexadecimal string back to the original text.

    Parameters:
    - hex_string (str): The hexadecimal string to convert.

    Returns:
    - str: The original text.
    """
    bytes_object = bytes.fromhex(hex_string)
    original_text = bytes_object.decode('utf-8')
    return original_text

# Example usage
original_text = "Hello from the other side"
hex_representation = text_to_hex(original_text)
print(f"Hexadecimal Representation: {hex_representation}")

# Convert back to original text
converted_text = hex_to_text(hex_representation)
print(f"Converted Back to Original Text: {converted_text}")
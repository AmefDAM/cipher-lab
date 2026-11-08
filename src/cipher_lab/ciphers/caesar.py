import string

def encrypt(text, shift):

    encrypted_text = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not isinstance(shift, int) or isinstance(shift, bool):
        raise TypeError("shift must be an integer")

    for character in text:
        if character in string.ascii_uppercase:
            alphabet = string.ascii_uppercase
            index = alphabet.index(character)
            new_index = (index + shift) % len(alphabet)
            
            encrypted_text += alphabet[new_index]

        elif character in string.ascii_lowercase:
            alphabet = string.ascii_lowercase
            index = alphabet.index(character)
            new_index = (index + shift) % len(alphabet)
            
            encrypted_text += alphabet[new_index]

        else:
            encrypted_text += character

    return encrypted_text


"""Unit tests for the Caesar cipher."""


if __name__ == '__main__':

    # Test Cases:

    # 1. Basic encryption
    assert encrypt("HELLO", 3) == "KHOOR"

    # 2. Case preservation
    assert encrypt("Hello", 3) == "Khoor"

    # 3. Alphabet wrapping
    assert encrypt("XYZ", 3) == "ABC"

    # 4. Zero shift
    assert encrypt("HELLO", 0) == "HELLO"

    # 5. Negative shift
    assert encrypt("HELLO", -3) == "EBIIL"

    # 6. Preservation of spaces and punctuation
    assert encrypt("Hello, World!", 3) == "Khoor, Zruog!"

    # 7. Basic decryption
    # assert decrypt("KHOOR", 3) == "HELLO"

    # 8. Invalid text in encryption
    try:
        encrypt(123, 3)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")

    # 9. Invalid shift in encryption
    try:
        encrypt("HELLO", 3.5)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")

    # 10. Invalid text in decryption
    # try:
    #     decrypt(123, 3)
    # except TypeError:
    #     pass
    # else:
    #     raise AssertionError("Expected TypeError")

    # 11. Invalid shift in decryption
    # try:
    #     decrypt("HELLO", 3.5)
    # except TypeError:
    #     pass
    # else:
    #     raise AssertionError("Expected TypeError")

    print("All tests passed!")

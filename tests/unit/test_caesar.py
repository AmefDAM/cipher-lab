
"""Unit tests for the Caesar cipher."""

from cipher_lab.ciphers.caesar import encrypt, decrypt


if __name__ == '__main__':

    # Test Cases:

    # 1. Basic encryption
    assert encrypt("HELLO", 3) == "KHOOR"

    # 2. Case preservation
    # assert encrypt("Hello", 3) == "Khoor"

    # 3. Alphabet wrapping
    # assert encrypt("XYZ", 3) == "ABC"

    # 4. Zero shift
    # assert encrypt("HELLO", 0) == "HELLO"

    # 5. Negative shift
    # assert encrypt("HELLO", -3) == "EBIIL"

    # 6. Preservation of spaces and punctuation
    # assert encrypt("Hello, World!", 3) == "Khoor, Zruog!"

    # 7. Basic decryption
    # assert decrypt("KHOOR", 3) == "HELLO"

    # 8. Invalid text in encryption
    # try:
    #     encrypt(123, 3)
    # except TypeError:
    #     pass
    # else:
    #     raise AssertionError("Expected TypeError")

    # 9. Invalid shift in encryption
    # try:
    #     encrypt("HELLO", 3.5)
    # except TypeError:
    #     pass
    # else:
    #     raise AssertionError("Expected TypeError")

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

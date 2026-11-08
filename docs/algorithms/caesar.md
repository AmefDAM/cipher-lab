# Caesar Cipher

## 1. Description

The Caesar cipher is a classical substitution cipher in which each letter in the plaintext is replaced by another letter located a fixed number of positions further along the alphabet.

The alphabet wraps around when its end is reached.

The cipher uses a numerical shift value, which determines how many positions each letter moves.

It is a monoalphabetic substitution cipher and is not considered cryptographically secure.

## 2. Mathematical Definition

Let:

- \(A\) be the alphabet.
- \(N\) be the number of characters in the alphabet.
- \(x\) be the numerical position of a plaintext character, starting at zero.
- \(k\) be the shift value.
- \(E(x)\) be the encrypted character position.
- \(D(x)\) be the decrypted character position.

Encryption:

\[
E(x) = (x + k) \bmod N
\]

Decryption:

\[
D(x) = (x - k) \bmod N
\]

The modulo operation ensures that the transformation wraps around the alphabet.

## 3. Input Parameters

| Parameter | Type | Description |
|---|---|---|
| `text` | String | The text to encrypt or decrypt. |
| `shift` | Integer | The number of positions by which letters are shifted. |
| `alphabet` | String | The ordered set of characters used by the cipher. |

### Default Alphabet

The initial implementation uses the English alphabet:

`ABCDEFGHIJKLMNOPQRSTUVWXYZ`

The alphabet should be configurable in future versions.

## 4. Transformation Rules

The algorithm follows these rules:

1. Each character is checked against the selected alphabet.
2. Characters belonging to the alphabet are transformed according to the shift value.
3. Characters not belonging to the alphabet remain unchanged.
4. Uppercase and lowercase letters retain their original case.
5. Whitespace, punctuation and digits remain unchanged.
6. The transformation wraps around the alphabet when necessary.

## 5. Encryption Behaviour

Encryption moves each alphabetic character forward by the specified shift value.

Example:

- Plaintext: `HELLO WORLD`
- Shift: `3`
- Ciphertext: `KHOOR ZRUOG`

Another example:

- Plaintext: `Hello, World!`
- Shift: `3`
- Ciphertext: `Khoor, Zruog!`

## 6. Decryption Behaviour

Decryption reverses the encryption process by moving each alphabetic character backwards by the specified shift value.

Example:

- Ciphertext: `KHOOR ZRUOG`
- Shift: `3`
- Plaintext: `HELLO WORLD`

Decryption should restore the original text when using the same alphabet and shift value used during encryption.

## 7. Constraints and Expected Errors

The algorithm must validate its input parameters before performing any transformation.

### Text

- Must be a string.
- Empty strings are valid inputs.
- Non-string values should raise a `TypeError`.

### Shift

- Must be an integer.
- Negative integers are valid.
- Zero is valid.
- Values greater than the alphabet length are valid and should wrap around.
- Non-integer values should raise a `TypeError`.

### Alphabet

- Must be a non-empty string.
- Must not contain duplicate characters.
- Must contain characters that can be handled consistently by the transformation rules.
- Invalid alphabets should raise a `ValueError`.

## 8. Expected Properties

The implementation should satisfy the following properties:

- Encrypting with a shift of zero returns the original text.
- Encrypting with a shift equal to the alphabet length returns the original text.
- Negative shifts are supported.
- Encrypting and then decrypting with the same shift restores the original text.
- Characters outside the alphabet remain unchanged.
- Character case is preserved.

## 9. Future Considerations

The following features are outside the scope of the initial implementation:

- User-defined alphabets through the graphical interface.
- Support for arbitrary Unicode alphabets.
- Automatic brute-force decryption.
- Frequency analysis.
- Cryptographic security.

These features may be considered in future versions.
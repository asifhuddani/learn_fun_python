alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#  Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
#  Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
#  Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         if letter not in alphabet:
#             cipher_text += letter
#         else:
#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position %= len(alphabet)
#             cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#
# def decrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         if letter not in alphabet:
#             cipher_text += letter
#         else:
#             shifted_position = alphabet.index(letter) - shift_amount
#             shifted_position %= len(alphabet)
#             cipher_text += alphabet[shifted_position]
#     print(f"Here is the decoded result: {cipher_text}")

def caesar(direction_chose,text_to_act, shift_to_do):
    if direction_chose == 'decode':
        shift_to_do *= -1

    cipher_text = ""
    for letter in text_to_act:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_to_do
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

caesar(direction, text, shift)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Enter your message: ").lower()
shift = int(input("Enter how many shift you want: "))


def Cipher(start_new, shift_number, new_direction):
    end_text = ""
    if new_direction == "decode":
        shift_number *= (-1)
    for letter in start_new:
        position = alphabet.index(letter)
        new_position = position + shift_number
        new_letter = alphabet[new_position]
        end_text += new_letter
    print(f"Your new, {direction}d text is , {end_text}")
    
Cipher(start_new=text, shift_number=shift, new_direction=direction)
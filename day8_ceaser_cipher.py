from ascii_art import cipher_ascii_art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type encode to encrypt and type decode to decrypt:\n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type your shift number: \n"))

def ceaser(output_text, shift_amount, encode_or_decode):
    result_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in output_text:
        shift_pos = alphabet.index(letter) + shift_amount # e.g. 9 > 7 return letter index by minusing shift amount
        shift_pos %= len(alphabet)
        result_text += alphabet[shift_pos]
        
    print(f"Here is the {encode_or_decode}d result: {result_text}")    

cipher_ascii_art()
ceaser(output_text=text, shift_amount=shift, encode_or_decode=direction)

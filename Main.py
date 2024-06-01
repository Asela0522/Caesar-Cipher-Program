Letters ="abcdefghijklmnopqrstuvwxyz"
print("**** CAESAR CIPHER PROGRAM ****")
print("Do you wanted to Encrypt or Decrypt ? ")
user_input =input('Please Enter (e/d): ').lower()

Num_Letters =len(Letters)

def encrypt(plaintext,key):
    ciphertext =''
    for letter in plaintext:
        letter =letter.lower()
        if not letter == " ":
            index =Letters.find(letter)
            if index == -1:
                ciphertext +=letter
            else:
                New_index =index + key
                if New_index >= Num_Letters:
                    New_index -=Num_Letters
                ciphertext += Letters[New_index]
    return ciphertext


def decrypt(ciphertext,key):
    plaintext =''
    for letter in ciphertext:
        letter =letter.lower()
        if not letter == " ":
            index =Letters.find(letter)
            if index == -1:
                plaintext +=letter
            else:
                New_index =index - key
                if New_index <0 :
                    New_index +=Num_Letters
                plaintext += Letters[New_index]
    return plaintext


if user_input == "e":
    print()
    print("ENCRYPTION MODE SELECTED.")
    key =int(input("Enter the key (1 trough 26):"))
    Text =input("Enter the text to encrypt:")
    ciphertext =encrypt(Text,key)
    print(f"CIPHER TEXT:{ciphertext}")

elif user_input == "d":
    print()
    print("DECRYPTION MODE SELECTED.")
    key =int(input("Enter the key (1 trough 26):"))
    Text =input("Enter the text to decrypt:") 
    plaintext =decrypt(Text,key)
    print(f"PLAIN TEXT:{plaintext}")   
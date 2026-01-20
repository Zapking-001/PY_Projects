"""
Docstring for 21.Caeser Cipher: This is a sort of Encoding and decoding in which teh value of a Letter is moved by a key value either ∓Key. It is actually one of my favorite.

         Example: 
                    A B C D E F G H I J  K  L
                    1 2 3 4 5 6 7 8 9 10 11 12
                Word: DIE ; key = +2
                Then we will move the letters by 2 units, 
                        D -> F
                        I -> K
                        E -> G
                Therefore resultant Word is, FKG.
        
         Efficiency: Time complexity is O(n)
                     Space complexity is O(n)
                     Where n is the length of the string.
"""

s = input("Enter a word / phrase: ")
key = int(input("Enter shift value: "))
while True:
    try:
        mode = input("Enter mode (Encode/Decode): ").lower()
        if mode not in ['e', 'd']:
            raise ValueError()
        else:
            break
    except:
        print("Expected input 'E' or 'D'\n")

def caesar_cipher(text, shift, encode=True):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            if encode:
                result += chr((ord(ch) - base + shift) % 26 + base)
            else:
                result += chr((ord(ch) - base - shift) % 26 + base)
        else:
            result += ch  # keep spaces/punctuation unchanged
    return result

if mode == 'e':
    print("Encoded:", caesar_cipher(s, key, encode=True))
else:
    print("Decoded:", caesar_cipher(s, key, encode=False))

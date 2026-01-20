"""
Docstring for 24.Pangram : A phrase / sentence which contains all the letter's present in the Alphabets.

    Ex: "Pack my box with five dozen liquor jugs"
        "The quick brown fox jumps over the lazy dog"
        "Zapking hacker mix C++, JavaScript, Python, Linux, and quirky web DevOps to fix bugs."
    Mathematical Defination :  s is said to be a pangram iff ∀ a ∈ set(Alphabets), a ∈ letters(s).

    Efficiency: Time complexity is O(n)
                Space complexity is O(1)
                Where n is the length of the string
"""

s = input("Enter a phrase: ").lower()
alphabets = set('abcdefghijklmnopqrstuvwxyz')

def Pangram(k):
    return alphabets.issubset(k)

if Pangram(s):
    print(f"It is a Pangram")
else:
    print(f"It is not a Pangram")

#   OR 

if set(s.lower()) >= alphabets:
    print(f"It is a Pangram")
else:
    print(f"It is not a Pangram")

#  OR

for ch in alphabets:
    if ch not in s.lower():
        print(f"It is not a Pangram")
        break
else:
    print(f"It is a Pangram")


# If have provided Three methodology's of Implementing and Evaluating a Pangram, All will result the same answer, Check if you want.
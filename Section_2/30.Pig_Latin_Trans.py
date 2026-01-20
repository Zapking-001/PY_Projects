"""
Docstring for 30.Pig_Latin_Trans

        Efficiency: Time complexity is O(n)
                    Space complexity is O(n)
                    Where n is the length of the string.

"""
def pig_latin(word):
    vowels = "aeiou"
    if word[0].lower() in vowels:
        return word + "ay"
    else:
        for i, ch in enumerate(word):
            if ch.lower() in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"

s = input("Enter a word: ")
print(f"Translated word : {pig_latin(s)}")

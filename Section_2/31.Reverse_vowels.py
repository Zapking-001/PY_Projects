"""
Docstring for 31.Reversing Vowels: This program starts to move from both the ends simultaneously, and uses Two-pointer swap technique until found a vowel in either side and then will gets replaced.
        Ex: 
                Word = "hello"
                        S-1 : i=0 'h' & j=4 'o'
                        S-2 : i=1 'e' & j=4 'o' now both are Vowels, then it gets swapped
                        S-3 : i=2 'l' & j=3 'l'
                        S-4 : No more swaps left, hence it results 'holle'
        
        Efficiency: Time complexity is O(n)
                    Space complexity is O(1)


"""
def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
    return "".join(s)

s = input("Enter a string: ")

print(f"Result: {reverse_vowels(s)}")
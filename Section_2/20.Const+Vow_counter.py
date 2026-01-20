"""
Docstring for 20.Const+Vow_counter: Thi program counts the total number of Vowels & Consonants present in the String, for evaluation we choose a List ls containing the Vowels in lowercase.

        Efficiency: Time complexity is O(n)
                    Space complexity is O(1)
                    Where n is the length of the string.
"""
ls = ['a', 'e', 'i', 'o', 'u']

s = input("Enter a string: ").lower()
vow,cons = 0,0

for ch in s:
    if ch in ls:
        vow +=1
    else:
        cons +=1

print(f"Total number of Vowels: {vow}")
print(f"Total number of Consonants: {cons}")
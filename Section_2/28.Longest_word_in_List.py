"""
Docstring for 28.Longest word in List: This program returns the longest word in the List.

        Efficiency: Time complexity is O(n)
                    Space complexity is O(1)
                    Where n is the length of the string.


"""
def longest_word(k):
    longest = ""
    for word in k:
        if len(word) > len(longest):
            longest = word
    return longest.capitalize()

wordslist = input("Enter the values of List: ").split()

print(f"The longest word is: {longest_word(wordslist)}")

print(f"The longest word is: {max(wordslist, key=len)}") # The Second shortest way

'''
print(f"The longest word is: {max(input("Enter the values of List: ").split(), key=len)}")
'''
# Ultimate Single line command to perform it.
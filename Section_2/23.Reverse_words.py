"""
Docstring for 23.Reverse_words in a phrase .
        Ex: "I love python programming" -> "programming python love I"
    Steps:

        1. Split → ["I", "love", "Python", "programming"]

        2. Reverse → ["programming", "Python", "love", "I"]

        3. Join → "programming Python love I" by using " " as a separator.

        Efficiency: Time complexity is O(n)
                    Space complexity is O(n)
                    Where n is the length of the string.

"""
s = input("Enter a sentence: ").split()

# s_new = []
# for word in s[::-1]:
#     s_new.append(word)

print(f"Reversed phrase : {" ".join(s[::-1])}") # we can replace s[::-1] -> s_new { If we perform the looping for reverse }

# The above represents we can write the code in either 2 lines or atleast 3 lines.
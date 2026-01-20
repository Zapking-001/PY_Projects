"""
Docstring for 29.Punctuation

        Efficiency: Time complexity is O(n)
                    Space complexity is O(n)
                    Where n is the length of the string.

"""
import string
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

phrase = input("Enter the sentence or Paragraph: ")

print("Below we can see the Sentence or the Paragraph from which All the 'PUNCTUATIONS' are removed: \n")
print(remove_punctuation(phrase))





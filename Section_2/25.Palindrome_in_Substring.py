"""
Docstring for 25.Palindrome in Substring: A part of String which is the longest and it must be Palindrome.

        Ex: 
            1.DEVELOPER  ---> EVE is the only possible & longest Palindrome.
            2.aaadbcccccg --> ccccc is the longest Palindromic Substring, even though aaa is a Palindromic substring, is it the second longest. Hence 'aaa' cannot be the answer.

        
        Efficiency: Time complexity is O(n²)
                    Space complexity is O(1)
                    Where n is the length of the string.

"""
def longest_palindromic_substring(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]  # substring after expansion
    
    longest = ""
    for i in range(len(s)):
        # Odd length palindrome
        odd = expand(i, i)
        # Even length palindrome
        even = expand(i, i+1)
        
        # Update longest
        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even
    
    return longest

# Example usage
s = input("Enter a string: ")
result = longest_palindromic_substring(s)
print("Longest palindromic substring:", result)

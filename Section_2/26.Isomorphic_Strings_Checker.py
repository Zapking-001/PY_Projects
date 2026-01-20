"""
Docstring for 26.Isomorphic Strings: 
        Two strings are isomorphic if the characters in one string can be replaced to get the other string, with the following rules:

            1. Each character in the first string must map to exactly one character in the second string.
            2. No two characters from the first string can map to the same character in the second string.
            3. The mapping must be consistent across the entire string.
        
        Ex: egg & add 
                if e -> a && g -> d, Then both are isomorphic.
            foo & bar
                if f -> b && o -> a, Then both are not isomorphic, because the last letter is not a, but r.
                
        Efficiency: Time complexity is O(n)
                    Space complexity is O(1)
                    Where n is the length of the string.

"""
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    mapping_s = {}
    mapping_t = {}
    
    for c1, c2 in zip(s, t):
        if c1 in mapping_s and mapping_s[c1] != c2:
            return False
        if c2 in mapping_t and mapping_t[c2] != c1:
            return False
        mapping_s[c1] = c2
        mapping_t[c2] = c1
    
    return True
str1, str2 = map(str, input("Enter two strings: ").split())

if is_isomorphic(str1, str2):
    print(f"{str1} and {str2} are isomorphic.")
else:
    print(f"{str1} and {str2} are not isomorphic.")
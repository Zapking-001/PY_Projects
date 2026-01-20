"""
Docstring for 18.Anagrams : Two strings are anagrams if they contain the same characters with the same frequency, but possibly in a different order.
                            Which means, It two words have same letters but rearranged to make a different word.

                Ex:  LISTEN & SILENT ; If we sort it, We get EILNST for both which is true.

                Efficiency: Time complexity is O(n+m)
                            Space complexity is O(1)

                            Where n, m are the lengths of two strings.
"""

str1, str2 = map(str, input("Enter two strings: ").split())

if sorted(str1) == sorted(str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")
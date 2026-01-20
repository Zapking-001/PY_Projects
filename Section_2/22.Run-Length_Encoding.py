"""
Docstring for 22.Run-Length Encoding: : Replace runs by symbol+count, e.g. AAAB → A3B1 (compress contiguous equal chars)

        Efficiency: Time complexity is O(n)
                    Space complexity is O(n)
                    Where n is the length of the string.
"""
s = input("Enter a string: ")

def run_length_encoding(text):
    if not text:
        return ""
    
    result = ""
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            result += text[i-1] + str(count)
            count = 1
    result += text[-1] + str(count)  # add last group
    
    return result

print("RLE:", run_length_encoding(s))

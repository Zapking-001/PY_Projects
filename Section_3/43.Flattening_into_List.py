"""
Docstring for 43.Flattening_into_List: We are converting 2-D array / matrix -> 1-D array / list

            Efficiency : Time complexity: O(n)
                         Space complexity: O(d)

"""
rows, cols = map(int, input("Enter number of rows & columns: ").split())

print("Enter a Row by pressing enter & Column elements separated by space:")
A = [list(map(int, input().split())) for _ in range(rows)]

# Method - 1
def flatten_list(nested_list):
    flat = []
    for sublist in nested_list:
        for item in sublist:
            flat.append(item)
    return flat


result = flatten_list(A)
print(result)

# Method - 2
print([x for sub in A for x in sub])

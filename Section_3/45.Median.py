"""
Docstring for 45.Median
        Efficiency : Time complexity: O(nlog n)
                     Space complexity: O(1)
"""
from statistics import median
ls = input("Enter the objects: ").split()
for words in range(len(ls)):
    if ls[words].isdigit():
        ls[words] = int(ls[words])

def median(arr):
    arr = sorted(arr)
    n = len(arr)
    mid = n // 2
    return arr[mid] if n % 2 else (arr[mid - 1] + arr[mid]) / 2

print(median(ls))
print(f"Median: {median(ls)}")

"""
Docstring for Section_3.49.Subarray_Sum
"""

# Method - 1

def subarray_sum_efficient(arr, target):
    curr_sum = 0
    start = 0
    for end in range(len(arr)):
        curr_sum += arr[end]
        while curr_sum > target and start < end:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == target:
            return (start, end)
    return None

# Method - 2

def s_subsum(arr, t):
    return [(i, j) for i in range(len(arr)) for j in range(i, len(arr)) if sum(arr[i:j+1]) == t]

# Method - 3

def subarray_sum_math(arr, target):
    prefix_map = {0: -1}
    curr_sum = 0
    for i, x in enumerate(arr):
        curr_sum += x
        if (curr_sum - target) in prefix_map:
            return (prefix_map[curr_sum - target] + 1, i)
        prefix_map[curr_sum] = i
    return None

# Test cases
arr = [1, 4, 20, 3, 10, 5]
target = 33
print(f"Efficient method: {subarray_sum_efficient(arr, target)}")
print(f"Simple method: {s_subsum(arr, target)}")
print(f"Math method: {subarray_sum_math(arr, target)}")

arr = [1, 2, 3, 7, 5]
target = 12
print(f"Efficient method: {subarray_sum_efficient(arr, target)}")
print(f"Simple method: {s_subsum(arr, target)}")
print(f"Math method: {subarray_sum_math(arr, target)}")

arr = [10, 2, -2, -20, 10]
target = -10
print(f"Efficient method: {subarray_sum_efficient(arr, target)}")
print(f"Simple method: {s_subsum(arr, target)}")
print(f"Math method: {subarray_sum_math(arr, target)}")

arr = [-10, 0, 10, 20]
target = 20
print(f"Efficient method: {subarray_sum_efficient(arr, target)}")
print(f"Simple method: {s_subsum(arr, target)}")
print(f"Math method: {subarray_sum_math(arr, target)}")
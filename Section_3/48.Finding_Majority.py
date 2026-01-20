"""
Docstring for Section_3.49.Finding_Majority

            Efficiency : Time complexity: O(n)
                         Space complexity: O(1)
                         Where n is the number of elements in the list.
"""

# Method - 1

def majority_efficient(nums):
    candidate = None
    count = 0
    for x in nums:
        if count == 0: candidate = x
        count += (1 if x == candidate else -1)
    # Verification pass
    return candidate if nums.count(candidate) > len(nums) // 2 else None

# Method - 2

def s_majority(l):
    cand = sorted(l)[len(l)//2]
    return cand if l.count(cand) > len(l)//2 else None

# Method - 3

def majority_math(nums):
    counts = {}
    n = len(nums)
    for x in nums:
        counts[x] = counts.get(x, 0) + 1
        if counts[x] > n // 2:
            return x
    return None


# Test cases
arr = [2, 2, 1, 1, 1, 2, 2]
print(f"Efficient method: {majority_efficient(arr)}")
print(f"Simple method: {s_majority(arr)}")
print(f"Math method: {majority_math(arr)}")

arr = [3, 2, 3]
print(f"Efficient method: {majority_efficient(arr)}")
print(f"Simple method: {s_majority(arr)}")
print(f"Math method: {majority_math(arr)}")

arr = [1]
print(f"Efficient method: {majority_efficient(arr)}")
print(f"Simple method: {s_majority(arr)}")
print(f"Math method: {majority_math(arr)}")

arr = [1, 2, 3, 4, 5]
print(f"Efficient method: {majority_efficient(arr)}")
print(f"Simple method: {s_majority(arr)}")
print(f"Math method: {majority_math(arr)}")

arr = [6, 5, 5]
print(f"Efficient method: {majority_efficient(arr)}")
print(f"Simple method: {s_majority(arr)}")
print(f"Math method: {majority_math(arr)}")
"""
Docstring for 58.Pascals_Triangle: 

Given an integer numRows, return the first numRows of Pascal's triangle.

The Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1

            Efficiency : Time complexity: O(n²)
                         Space complexity: O(n)

"""
# Method - 1
n = int(input("Enter the Range: "))
def pascal_triangle(n):
    if n <= 0:
        return "Value should be greater than 0"
    triangle = [[1]*(i+1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle

if n>=0:
  for row in pascal_triangle(n+1):
    print("  ".join(map(str,row)))
elif n<0:
  print(pascal_triangle(n))

# Method - 2
import math

def pascal_triangle(n):
    return [[math.comb(i, j) for j in range(i+1)] for i in range(n)]

for row in pascal_triangle(n+1):
    print("  ".join(map(str,row)))


# Method - 3
def factorial(x):
    return 1 if x == 0 else x * factorial(x-1)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

def pascal_triangle_math(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i+1):
            row.append(nCr(i, j))
        triangle.append(row)
    return triangle

for row in pascal_triangle_math(n):
    print(row)

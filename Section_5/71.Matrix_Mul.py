"""
Docstring for 71.Matrix_Mul

                    Efficiency: Time complexity = O(n³)
                                Space complexity = O(n²)
"""
# Method - 1
def matrix_mult_efficient(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    if cols_A != rows_B:
        raise ValueError("Dimensions mismatch: cols of A must equal rows of B.")
        
    # Pre-allocate result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

#---------------------------------------------------------------------#

# Method - 2
def matrix_mult_shortest(A, B):
    return [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

# Example: matrix_mult_short([[1, 2]], [[3], [4]]) -> [[11]]

#---------------------------------------------------------------------#

# Method - 3
def matrix_mult_math(A, B):
    # Strictly following the summation notation C_ij = Σ (A_ik * B_kj)
    rows = range(len(A))
    cols = range(len(B[0]))
    inner = range(len(B))
    
    return [[sum(A[i][k] * B[k][j] for k in inner) for j in cols] for i in rows]

# Example: Same as above

rows_A, cols_A = map(int, input("Enter number of rows & columns for Matrix A: ").split())
print("Enter elements for Matrix A:")
A = [list(map(int, input().split())) for _ in range(rows_A)]

rows_B, cols_B = map(int, input("Enter number of rows & columns for Matrix B: ").split())
print("Enter elements for Matrix B:")
B = [list(map(int, input().split())) for _ in range(rows_B)]

print("\nMatrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

try:
    result_efficient = matrix_mult_efficient(A, B)
    print("\nResult (Efficient Method):")
    for row in result_efficient:
        print(row)

    result_shortest = matrix_mult_shortest(A, B)
    print("\nResult (Shortest Method):")
    for row in result_shortest:
        print(row)

    result_math = matrix_mult_math(A, B)
    print("\nResult (Mathematical Method):")
    for row in result_math:
        print(row)

except ValueError as e:
    print(f"\nError: {e}")  
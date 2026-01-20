"""
Docstring for 41.Transpose_of_Matrix
        Ex:
            Input:
                Matrix is:
                1 2 3
                4 5 6
            Output:
                Transpose Matrix: 
                1 4 
                2 5 
                3 6 

            Efficiency : Time complexity: O(m•n)
                         Space complexity: O(m•n)
                         Where m is the number of rows and n is the number of columns.

"""

# Method - 1
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

rows, cols = map(int, input("Enter number of rows & columns: ").split())
print("Enter a Row by pressing enter & Column elements separated by space:")
matrix = [list(map(int, input().split())) for _ in range(rows)]

A = transpose_matrix(matrix)

print("Transpose Matrix: ",end="")
for row in A:
    print(" ".join(map(str, row)))
    print(" "*18,end="")                        # For Alignment

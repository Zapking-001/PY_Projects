"""
        Ex: Here is an example of Input Idea in which user must input the Matrix.

        %   Method - 1   %                                           %   Method - 2   %
            Input:                                                  |   Input:     
                Enter number of rows: 2                             |           Enter number of rows & columns: 2,3 
                Enter number of columns: 3                          |           
                Enter row 1 elements separated by space: 1 2 3      |           1 2 3
                Enter row 2 elements separated by space: 4 5 6      |           4 5 6
            Output:                                                 |
                Matrix is:                                          |
                [1, 2, 3]                                           |
                [4, 5, 6]                                           | 


"""
# Method - 1
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
    matrix.append(row)

print("Matrix is:")
for r in matrix:
    print(r)

# Method - 2
rows, cols = map(int, input("Enter number of rows & columns: ").split())
print("Enter a Row by pressing enter & Column elements separated by space:")
matrix = [list(map(int, input().split())) for _ in range(rows)]

print("Matrix is:")
for ele in matrix:
    print(ele)

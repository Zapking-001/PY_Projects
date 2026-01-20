"""
Docstring for 40.Matrix_Addition: This program focuses on Matrix's primitive operation i.e. Addition.

            Efficiency : Time complexity: O( m•n )
                         Space complexity: O( m•n )
"""

rows, cols = map(int, input("Enter number of rows & columns: ").split())

print("\nEnter a Row by pressing enter & Column elements separated by space:")
A = [list(map(int, input().split())) for _ in range(rows)]

print("\nEnter a Row by pressing enter & Column elements separated by space:")
B = [list(map(int, input().split())) for _ in range(rows)]


# Method - 1

def matrix_addition(A, B):
    rows, cols = len(A), len(A[0])
    result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
    return result

C = matrix_addition(A, B)

if rows and cols == 2:
    print("─"*50)
    print("┌─"," "*(2*cols-1),"─┐")
    [print("│","  ".join(map(str,ele))," │") for ele in C]
    print("└─"," "*(2*cols-1),"─┘")
    quit()  

for ele in C:
    [print(" ".join(f"{num:3}" for num in ele),"\n")]

print("─"*50)
# Method - 2
C = [[a+b for a,b in zip(r1,r2)] for r1,r2 in zip(A,B)]
for row in C:
    print("  ".join(f"{num:3}" for num in row)+"\n")

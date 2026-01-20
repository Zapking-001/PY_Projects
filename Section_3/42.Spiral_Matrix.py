"""
Docstring for 42.Spiral_Matrix
        Ex:            
        Input:
                Enter the range: 3

        Output:
                Matrix: 
                  1  2  3
                  8  9  4
                  7  6  5

            Efficiency : Time complexity: O(n²)
                         Space complexity: O(1)
                         Where n is the number of rows or columns.
                         

"""
# Method - 1
def spiral(n):
    m=[[0]*n for _ in range(n)]
    t,l,b,r=n-1,0,n-1,n-1;i=1
    print("Matrix: \n")
    while l<=r and l<=b:
        for j in range(l,r+1):m[l][j]=i;i+=1
        for k in range(l+1,b+1):m[k][r]=i;i+=1
        for j in range(r-1,l-1,-1):m[b][j]=i;i+=1
        for k in range(b-1,l,-1):m[k][l]=i;i+=1
        l+=1;r-=1;b-=1
    w=len(str(n*n))
    [print(" ".join(f"{x:{w}}" for x in row)) for row in m]

spiral(int(input("Enter the range: ")))

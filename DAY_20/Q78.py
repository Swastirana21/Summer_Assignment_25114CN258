# Check symmetric matrix 
def is_symmetric(A):
    n=len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j]!=A[j][i]:
                return False
    return True
A=[[1,2,3],[2,5,6],[3,6,9]]
print("Is symmetric:",is_symmetric(A))

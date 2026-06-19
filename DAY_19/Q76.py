# Find diagonal sum 
def diagonal_sum(A):
    n=len(A)
    total=0
    for i in range(n):
        total+=A[i][i]
        total+=A[i][n-i-1]
    if n%2==1:
        total-=A[n//2][n//2]
    return total
A=[[1,2,3],[4,5,6],[7,8,9]]
print("Diagonal sum:",diagonal_sum(A))



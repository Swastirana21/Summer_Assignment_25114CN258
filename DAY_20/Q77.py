# Multiply matrices 
def multiply_matrices(A,B):
    rows_A=len(A)
    cols_A=len(A[0])
    cols_B=len(B[0])
    result=[[0]*cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j]+=A[i][k]*B[k][j]
    return result
A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
print("Matrix multiplication:",multiply_matrices(A,B))

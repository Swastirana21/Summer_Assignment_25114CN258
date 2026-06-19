# Transpose matrix 
def transpose_matrix(A):
    rows=len(A)
    cols=len(A[0])
    result=[[A[j][i] for j in range(rows)] for i in range(cols)]
    return result
A=[[1,2,3],[4,5,6]]
print("Transpose:",transpose_matrix(A))

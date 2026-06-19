# Subtract matrices 
def subtract_matrices(A,B):
    rows=len(A)
    cols=len(A[0])
    result=[[A[i][j]-B[i][j] for j in range(cols)]for i in range(rows)]
    return result
A=[[9,8],[7,6]]
B=[[1,2],[3,4]]
print("Matrix subtraction:",subtract_matrices(A,B))

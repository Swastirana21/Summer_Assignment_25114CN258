# Add matrices 
def add_matrices(A,B):
    rows=len(A)
    cols=len(A[0])
    result=[[A[i][j]+B[i][j] for j in range(cols)]for i in range(rows)]
    return result
A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
print("Matrix addition:",add_matrices(A,B))

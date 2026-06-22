# Find column-wise sum 
def column_wise_sum(A):
    cols=len(A[0])
    return[sum(A[row][col] for row in range(len(A))) for col in range(cols)]
A=[[1,2,3],[4,5,6],[7,8,9]]
print("column-wise sum:",column_wise_sum(A))

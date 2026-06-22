# Find row-wise sum 
def row_wise_sum(A):
    return[sum(row) for row in A]
A=[[1,2,3],[4,5,6],[7,8,9]]
print("Row-wise sum:",row_wise_sum(A))

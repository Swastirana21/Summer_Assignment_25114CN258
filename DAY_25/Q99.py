# Sort names alphabetically 
def sort_names(names):
    n=len(names)
    for i in range(n-1):
        for j in range(n-i-1):
            if names[j]>names[j+1]:
                names[j],names[j+1]=names[j+1],names[j]
    return names
names=["Ravi","Amit","Suresh","Priya","Kiran"]
print(sort_names(names))

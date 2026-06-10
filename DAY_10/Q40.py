# Character pyramid
rows=5
for i in range(1,rows+1):
    print(" "*(rows-i),end="")

    for j in range(i):
        print(chr(65+j),end="")

    for j in range(i-2,-1,-1):
        print(chr(65+j),end="")
    print()
N = int(input())
row = 0
col = (N-1)
n = 1
N1 = int((N+1)/2)

list1 = [[0 for i in range(N)] for j in range(N)]

for i in range(0,N1):
    for j in range(row,col+1):
        list1[row][j] = n
        n= n+1
    for j in range(row+1,col+1):
        list1[j][col] = n
        n = n + 1
    for j in range(col-1,row-1,-1):
        list1[col][j] = n 
        n = n + 1 
    for j in range(col-1,row,-1):
        list1[j][row] = n 
        n = n + 1 
    row = row + 1
    col = col - 1

for i in range(0,N):
    each_row = ""
    item = list1[i]
    for k in item:
        each_row = each_row + str(k)+" "
    print(each_row)
row=int(input())
col=int(input())
for i in range(row):
    for j in range(col):
        if i==0 or i==row-1 or j==0 or j==col-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()


'''
n=int(input())
for row in range(0,n+1):
    for col in range(0,n+1):
        if (row+col==3) or (col-row==3) or (row+col==9) or (row-col==3):
            print("*",end='')
        else:
            print(" ",end='')

    print()
'''
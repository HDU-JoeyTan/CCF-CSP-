digit='0123456789'
def rank(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    rank=0
    for col in range(cols):
        pivot_row=None
        for row in range(rank,rows):
            if matrix[row][col]!=0:
                pivot_row=row
                break
        if pivot_row is None:
            continue
        matrix[rank],matrix[pivot_row]=matrix[pivot_row],matrix[rank]
        pivot=matrix[rank][col]
        for j in range(col,cols):
            matrix[rank][j]/=pivot
        for row in range(rank+1,rows):
            if matrix[row][col]!=0:
                factor=matrix[row][col]
                for j in range(col,cols):
                    matrix[row][j]-=factor*matrix[rank][j]
        rank+=1
    return rank

def check(num,fm):
    goucheng = []
    for i in range(len(fm)):
        goucheng.append({})
        element=fm[i]+'#'
        index=0
        for j in range(len(element)-1):
            if element[j] in digit and element[j+1] not in digit:
                e=element[index:j+1]
                for k in range(len(e)):
                    if e[k] in digit:
                        e=[e[0:k],int(e[k:])]
                        break
                index=j+1
                if e[0] in goucheng:
                    goucheng[i][e[0]]+=e[1]
                else:
                    goucheng[i].update({e[0]:e[1]})
    yuansu=[]
    for i in range(len(goucheng)):
        yuansu=list(set(yuansu)|set(goucheng[i].keys()))
    matrix=[]
    for i in range(len(goucheng)):
        matrix.append([0 for j in range(len(yuansu)+1)])
        for j in range(len(yuansu)):
            if yuansu[j] in goucheng[i]:
                matrix[-1][j]+=goucheng[i][yuansu[j]]
    r=rank(matrix)
    if r<len(goucheng):
        print('Y')
    else:
        print('N')





n=int(input())
for i in range(n):
    f=input().split()
    check(int(f[0]),f[1:])
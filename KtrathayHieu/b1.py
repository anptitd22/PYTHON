m,n=map(int,input().split())
a=[]
a.append([0 for _ in range(n+1)])
for i in range(m):
    b=list(map(int,input().split()))
    b.insert(0,0)
    a.append(b)
record=[]
cnt=0
f=[[0 for _ in range(n+1)] for _ in range(m+1)]
f2=a
for i in range(1,m+1):
    for j in range(1,n+1):
        if a[i][j]==0:
            f[i][j]=0
        else: 
            f[i][j] = min(min(f[i-1][j],f[i][j-1]),f[i-1][j-1])+1
            f2[i][j]+=f2[i-1][j]
        if cnt<f[i][j]:
            record=[]
            cnt=f[i][j]
            record.append([j-cnt+1,i-cnt+1,j,i])
        elif cnt==f[i][j]:
            record.append([j-cnt+1,i-cnt+1,j,i])
print('dien tich hinh vuong lon nhat:',cnt**2)
for x in record:
    print(f'[{x[0]}, {x[1]}], [{x[2]}, {x[3]}]')
cnt,record=0,[]
for i in range(1,m+1):
    for j in range(1,n+1):
        minn=f2[i][j]
        for l in range(j,0,-1):
            if f2[i][l]!=0:
                if minn>f2[i][l]:
                    minn=f2[i][l]
                if cnt < minn*(j-l+1):
                    record=[]
                    cnt=minn*(j-l+1)
                    record.append([l,i-minn+1,j,i])
                elif cnt==minn*(j-l+1):
                    record.append([l,i-minn+1,j,i])
            else:
                break 
print('dien tich hinh chu nhat lon nhat:',cnt)
for x in record:
    print(f'[{x[0]}, {x[1]}], [{x[2]}, {x[3]}]')
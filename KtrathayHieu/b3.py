# e=1,u=2,i=3,o=4,a=5
n=int(input())
cnt=0
def Try(s,t):
    if len(s)==n:
        global cnt
        cnt+=1
        print(s)
        return   
    if t == 1:
        Try(s+'a',5)
        Try(s+'i',3)
    elif t == 2:
        Try(s+'a',5)
    elif t == 3:
        Try(s+'e',1)
        Try(s+'u',2)
        Try(s+'o',4)
        Try(s+'a',5)
    elif t == 4:
        Try(s+'u',2)
        Try(s+'i',3)
    else:
        Try(s+'e',1)
Try('e',1)
Try('u',2)
Try('i',3)
Try('o',4)
Try('a',5)
print(cnt)
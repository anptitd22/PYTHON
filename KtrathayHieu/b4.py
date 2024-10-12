import re
a=''
while True:
    try: a+=input()
    except: break
b=re.split('[.?!,;]',a)
Word_freq = dict({})
for s in b:
    if len(s) == 0: continue
    res = s.split()
    for x in res:
        if x in Word_freq:
            Word_freq[x]+=1
        else:
            Word_freq[x]=1
sorted_Word_freq = sorted(Word_freq.items(),key = lambda x: -x[1])
for x,y in sorted_Word_freq:
    print(x,y)
    
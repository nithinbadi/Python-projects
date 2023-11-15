l=['d','1','f','0','w','a','4','q']
res=['0']
m=1000000
while True:
    for i in list(j for j in l if j not in res):
        #print(m)
        #print(res)
        if m >ord(i):
            m=ord(i)
    res.append(chr(m))
    m=100000
    if len(res)==len(l):
        break
print(res)
    
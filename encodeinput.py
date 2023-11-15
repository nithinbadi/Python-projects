s=input("Enter a text: ")
res=[]
for i in list(s):
    i=chr(ord(i)+3)
    res.append(i)

print(''.join(res))
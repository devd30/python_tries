'''string = 'america'
lst = []
L=len(string)

for i in range(L):
    count = 0
    for j in range(L):
        if (string[i] == string[j]):
            #print count
            count = count + 1
    lst.append((string[i],count))
    x=(((string[i],count)))
    print (set(x))
s=set(lst)
print s'''

st="abbac"
print (st[0])
print (st[2])
#def func(string):
#    x="".join(set(string))

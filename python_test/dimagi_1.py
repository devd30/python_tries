test="abbac"
#cabba
#for val in range(len(test)):
#    print test[val]
index = 0
pos=0
te=''
ab=list(test)
xy=[]

for i,n in enumerate(ab):
    #print i
    if i==0 or n !=ab[i-1]:
        print ab[i-1] # for reverse
        #print n # for removing duplicate
e=[ab[i-1] for i,n in enumerate(ab) if i==0 or n!=ab[i-1]]
bc=''.join(e)
print bc

def test_func(val):
    e=[val[i-1] for i,n in enumerate(val) if i==0 or n!=val[i-1]]
    bc=''.join(e)
    return bc

secon='abbbaa'
print test_func(secon)



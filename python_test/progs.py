####################################################################
'''
Find how many times a number appears in a range 
Example : 0 to 35, if we look for 2 it appears 14 times
Alina Canada
'''
kk=2
nn=35
count_occurences = 0
for val in range(0,nn+1):
    #print val
    #if (len(str(nn)) == 1) and (val == kk):
    if (val == kk) and len(str(val)) == 1:
        #if val == kk:
        count_occurences +=1
            #count_occurences +=1
    else:
        a=map(int,str(val))
        for vals in a:
            if vals == kk:
                count_occurences += 1

print count_occurences


kkk=2
nnn=35
count_occur = 0
for val in range(0,nnn+1):
    #print val
    #if (len(str(nn)) == 1) and (val == kk):
    if (val == kkk) and len(str(val)) == 1:
        #if val == kk:
        count_occur +=1
            #count_occurences +=1
    else:
        a=str(val)
        for vals in a:
            if int(vals) == kkk:
                count_occur += 1

print count_occur,"2"


#####################################################################            

#####################################################################
'''

Zala : Shuffle the input digit in such a way that the out if is one digit from the front
and second digit is from the last.
Example:
a=123456
output = 162534
a=130
Output = 103
'''

a=1234567
lis=map(int,str(a))

lis1=[]
count=0

for i in lis:
    lis1.append(i)    
    for index,j in enumerate(reversed(lis)):
        #print (index,j,"da")
        if index == count:           
           lis1.append(j)           
    count +=1
    if (len(lis) == len(lis1)):
        break
    elif (len(lis) <= len(lis1)):
        lis1.pop()
        break        
bc=''.join(map(str,lis1))
print int(bc)

#####################################################################




'''
odd=lis[::2]
even=lis[1::2]
print lis[::2],lis[1::2]

i=0
for val in (odd):
    print val
    lis1.append(val)
    for index,val2 in enumerate(reversed(even)):
            if index == i:
                lis1.append(val2)
    i +=1
            
'''
'''
for i,val in enumerate(lis):
    #print val
    print len(lis),"mm"
    bb=count-len(lis)+1
    print bb
    #lis1.append(val)
    if i % 2 == 0:
        lis1.append(lis[bb])
        print lis[bb],"yy"
        count +=1
    else:
        lis1.append(val)
        count +=1
'''


#S="We test coders. Give us a try?"
S="Forget CVs..Save time . x x "
#first_split=S.split('.')
deli=['.','?','!']
len_of_word = []
test_va=[]
count_va=0

for valss in range(len(deli)):
    print deli[valss],"2345"

'''
for val in deli:
    if val in S:
        first_split=S.split(val)
        count_va +=1
        second_del=deli[count_va]
        print second_del,"22"
        for vals in first_split:
            if (deli[count_va]) in vals:
                second_del=deli[count_va]
                second_split = vals.split(second_del)
                #count_va +=1
                print len(second_split),"111"
'''

if '.' in S:
    first_split = S.split('.')
    print first_split
    for val in first_split:
        print val,"etet"
        if '?' in val:
            second_split=val.split('?')
            print second_split,"yy"
            for vals in second_split:
                print vals
                if '!' in vals:
                    last_split=vals.split('!')
                    print last_split,"tt"
                    #test_va.extend(last_split)
                else:
                    test_va.append(vals)
        else:
            test_va.append(val)
for valss in test_va:
    get_len=len(valss.split())
    len_of_word.append(get_len)
print max(len_of_word)



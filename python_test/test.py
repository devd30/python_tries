def F(n):
    if n < 2:
        return n

  #if n == 0:
    #return 0

  #elif n == 1:
    #return 1

    else:
        a=(F(n-1) + F(n-2)) % 1000000
        return a

a=F(36)
print a
'''
if len(str(a)) > 6:
    b=(a) % 1000000
    print b
else:
    #print "%06d" % (a,)
    print('{:06}'.format(a))

'''
'''
d=0
e=1
    
#def check(n):
for x in range(8):
    c=d+e
    print c
    d=e
    e=c
''' 
'''
'''


'''
while True:
    try:
        a=pointer+lis[pointer]
        #print a
        pointer=a
        #print pointer,"p"
        counter +=1
        #print counter,"c"
        if counter > len(lis):
            print "-1"
            break
    except:
        print counter
        break

'''

def fib(n):
    if n < 2:
        return n
    
    current_fib, next_fib = 0, 1
    
    while n > 0:
        current_fib, next_fib = next_fib, current_fib + next_fib
        n -= 1
        print (n,current_fib, next_fib)    
    return current_fib

print fib(8)

C=[1,8,-3,0,1,3,-2,4,5]
B=6
'''
def solution(K,A):
    listt=[]
    for i in A:
        print i
        i=int(i)
        for j in A:
            j=int(j)
            if i+j == K:
                listt.append((i,j))
    print type(listt)
    
    return listt





x=solution(B,C)
print x
'''

D=[1,1,-1,1]

def solution(A):
    #while len(A)>0:
    for i in A:
        if A>=0:
            A[i] = A[i] + i
            print A[i]
    return (-1)
          

    
solution(D)

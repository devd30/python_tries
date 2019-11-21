#https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

def solution(A,K):
    if len(A) == 0:
        return A
    K = K % len(A)
    #print (A[-K:])
    #print (A[:-K])
    return (A[-K:]+ A[:-K]) #lst [start:]    # Items index=start through the rest of the array, lst [:end]      # All items from the beginning through index=end-1

#print solution([3, 8, 9, 7, 6],3)
#print solution([1,2,3,4],4)

#https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
def bin_gap(N):
    s=str(bin(N).strip("0b"))
    #print (s)

    zero=0
    temp=0

    for i in range(len(s)):
        if s[i] == '0':
            zero += 1
        else:
            if temp < zero:
                #print (temp,"212",zero)
                temp = zero
            zero = 0
    return temp

#print (bin_gap(20))

# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
def f_jump(x,y,d):
    distance= y - x
    if distance % d ==0:
        return distance//d
    else:
        return distance//d + 1

#print f_jump(10,85,30)

#https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
def perm_check(A):
    if set(A) == set(range(1,1+len(A))):
        return 1
    else:
        return 0


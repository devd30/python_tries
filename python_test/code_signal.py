'''
b = [2, 1, 3, 5, 3, 2]

def firstDuplicate(a):
   myset= set()
   for val in a:
        if val in myset:
            return val
        myset.add(val)
   return -1
               
print firstDuplicate(b)

s="abacabad"

def firstNotRepeatingCharacter(s):
    
    for val in s:
        if s.index(val) == s.rindex(val):
            return val
    return ("_")
print firstNotRepeatingCharacter(s)


a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

def rotateimage(a):
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            print a[i][j]
            #a[j][i], a[i][j]  = a[i][j], a[j][i]
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a
        
print rotateimage(a)
'''
b= [3, 1, 2, 3, 4, 5]
c=3
def removeKFromList(l, k):
    new_list = [val for val in l if val != k]
    return new_list
print removeKFromList(b, c)


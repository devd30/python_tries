#Linear Search

arra=[2,3,4,10,40]
x=11

def sear(arr,x):
    for i in range(0,len(arr)):
        if arr[i] == x:
            return i
    return -1

print sear(arra,x)

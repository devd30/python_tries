lis=[-4, 3, -9, 0, 4, 1, ]
length=6
def plusMinus(arr):
    p_count=0
    n_count=0
    z_count=0
    for val in arr:
        if val > 0:
            p_count += 1
        elif val < 0:
            n_count += 1
        else:
            z_count += 1

    occur = {}
    test=lambda:x
    
    
    return p_count,n_count,z_count
print plusMinus(lis)

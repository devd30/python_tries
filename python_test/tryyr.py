aa=['abc','cde','def']
bb=''

def check(a,b):
    for vals in a:
        b+=vals + "\n"
    return b
print check(aa,bb)
    

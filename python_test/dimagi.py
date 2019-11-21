a='abbac'
'''
def test_func(string):
    rev=a[::-1]
    
    print rev
    for vals in string:
        #print vals,"1"
        for new_vals in rev:
            #print new_vals,"2"
            if new_vals == vals:
                print (new_vals,vals)
                new_rev= rev.replace(new_vals,'',1)
                #print new_rev
            else:
                pass

test_func(a)
'''

import itertools
b=''.join(ch for ch, _ in itertools.groupby(a))
print b[::-1]

def test_func(string):
    dup_rem=''.join(ch for ch, _ in itertools.groupby(string))    
    print dup_rem[::-1]

test_func(a)

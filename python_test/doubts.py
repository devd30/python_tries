#test file to test doubts

for no in range(1,11):
	print no

#Range will print one less of range

x=[2,3,3,4,56,7,7,8,3,3,5,5,67,7,7]

print x[1:4]

#Slicing also will print one less than max limit slice


stri="messy"

'''
def contains_no_duplicates(string):
  letters = {}
  for letter in string:
          if letter in letters:
                  return False
letters[letter] = True
return True

print contains_no_duplicates(strin)
'''
'''
lett={}
for letter in strin:
        print letter
        if letter not in lett:
                lett[letter]= True
'''                
#        else:
#                lett[letter]=False
                #return True
'''
for k, v in lett.items():
        #print (k,':',v)
        if v == 'True':
                print "string has no duplicates value"
        else:
                print "string has duplicate values"
'''
'''
stri="messy"
def test_func(strin):
        lett={}
        for letter in strin:
                if letter not in lett:
                        lett[letter]= True:q
                        
                return "Sting has no duplicates"
print test_func(stri)                
'''
def check_unique(strin):
        if len(set(strin)) == len(strin):
                return "string is unique"
        else:
                return "String has duplicate character"

print (check_unique(stri))


a=0
b=1
for x in range(5):
        c=a+b
        print c
        a=b
        b=c

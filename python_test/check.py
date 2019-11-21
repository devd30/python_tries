'''values = map(int, raw_input().split(','))
print values
a=reduce(lambda x, y: x ^ y, values)
print a'''
'''
capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
for k in capitals.values():
    #print capitals[k],"is the capitalof ", k
    print k
'''
'''
def bubblesort(testlist):
    for passnum in range(len(testlist)-1,0,-1):
        print (passnum,"cc")
        for i in range(passnum):
            if testlist[i] > testlist[i+1]:
                temp=testlist[i]
                testlist[i]=testlist[i+1]
                testlist[i+1]= temp

alist = [54,26,93,17,77,31,44,55,20]
bubblesort(alist)
print alist
'''

'''
def insertion_sort(list):
    for val in list:
        j=list.index(val)
        print j
        while j>0:
            if list[j-1] > list[j]:
                list[j-1],list[j]=list[j],list[j-1]
            else:
                break
            j=j-1
alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print alist
'''
'''
def selection_sort(list):
    for i in range(len(list)):
        min_val = i
        for j in range(i+1,len(list)):
            if list[min_val] > list[j]:
                min_val=j
        list[i],list[min_val]=list[min_val],list[i]

alist = [54,26,93,17,77,31,44,55,20]
selection_sort(alist)
print alist
'''

for val in raw_input():
    print val

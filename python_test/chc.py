
'''
input_str = "112bbc23"

new_list = list()
output = list()
for i in input_str:
    if len(new_list) == 0 or i in new_list:
        new_list.append(i)
    else:
        output.append((len(new_list), new_list[0]))
        new_list = [i]
    output.append((len(new_list), new_list[0]))
print(output)
'''
#input_st="abbac"
input_st="abbbaa"

list_input=list(input_st)
new_list=list()
for i,val in enumerate(input_st):
    #print i,val
    if i==0:
        new_list.append(val)
    elif (input_st[i-1] != val) :
        new_list.append(val)
print "".join(new_list[::-1])

def adj_dup(vals):
    lst=list()
    for ind,val in enumerate(vals):
        if ind==0:
            lst.append(val)
        elif (vals[i-1] != val) :
            lst.append(val)
    ("".join(lst[::-1]))

print adj_dup(input_st)
              

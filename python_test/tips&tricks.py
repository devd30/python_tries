#for i in range(1,12):
#    print ([f"{i} odd", f"{i} even"][i%2==0])

n=5
fact=1
for i in range(1,n+1):
    fact = fact*i
print fact

def recur_factorial(n):
   """Function to return the factorial
   of a number using recursion"""
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

print recur_factorial(5)


open_list = ["[","{","("] 
close_list = ["]","}",")"] 
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop()
    print stack
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
string = "{[]{()}"
print(string,"-", check(string)) 

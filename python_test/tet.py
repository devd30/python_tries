'''def solution(S):
    for val in range(1,100):
        print val
'''

S="We test coders. Give us a try?"
a=S.split('.')
for val in a:
    #print val
    if "?" in val:
        print val

with open("D:\Downloads\cq_logs", "r") as file:
    data = file.read(2)
    
    for vals in data:
        print data
    #file.write("test")


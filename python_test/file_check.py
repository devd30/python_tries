import re
import string
with open("D:\other_details.txt") as f:
    for ind,line in enumerate(f):
        if re.search('(.*?)latest\-successful(.*?)', line):
            co=all(char in string.printable for char in line)
            print co,"check"
print co



        

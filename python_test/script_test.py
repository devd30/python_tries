import json
import datetime

today=datetime.datetime.today()

count=0

retention_days = int(input("Enter the no. days to retain file:"))
file_location = raw_input("Enter the file location:")


with open(file_location,'r') as file:
    data = json.load(file)
    for val in data:
        creation_date=(val['creationTimestamp']).rsplit('-',1)[0]
        date_format=datetime.datetime.strptime(creation_date, '%Y-%m-%dT%H:%M:%S.%f')    
        difference = today - date_format
        if int(str(difference).split(' ')[0]) >= retention_days:
            count +=1
print count
    
        

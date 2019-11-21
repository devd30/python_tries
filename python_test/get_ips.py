from datetime import datetime, timedelta

from collections import Counter

import subprocess

import re

# getting current and last hour
current_time=datetime.now()

print (current_time.strftime('%d/%h/%Y:%H:%M'))

last_hour_date_time = datetime.now() - timedelta(hours = 1)

last_hour=last_hour_date_time.strftime('%d/%h/%Y:%H:%M')

print last_hour

#Getting logs from the main log file and saving the required in /tmp
with open("/tmp/logs_file", "wb") as out:
	subprocess.call(["grep",last_hour,"/var/log/httpd/access_log","-A100000"], stdout=out)

#Counting the numbber of times each Ip exist in file
cnt = Counter()
ipre = re.compile(r'^(?P<ip>(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) - -')
with open("/tmp/logs_file") as infile:
    for line in infile:
        m = ipre.match(line)
        if m is not None:
            ip = m.groupdict()['ip']
            #print ip
            cnt[ip] += 1

#printing the output
for ip , times in cnt.most_common():
	#print ip , times
	with open("/tmp/logs_file","r") as f:
		for line in f:
			#print line
			if ip in line:
				print line[:-19]

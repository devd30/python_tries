import json
import requests
import unicodedata


test_dict=dict()
final_dict=dict()
r=requests.get("https://api.bitbucket.org/2.0/repositories/tutorials/tutorials.bitbucket.org/commits?pagelen=100")
json_data=r.json()
repo=['splitpractice', 'oauth-examples', 'markdowndemo', 'sourcetree-starter', 'sourcetree-starter-c', 'online-edit-starter', 'sourcetree-starter-b', 'merger', 'bucket-o-sand', 'tutorials.git.bitbucket.org', 'git-site-content']

for commit in (json_data['values']):
    user=(commit['author']['raw']).split("<")[0]
    if (type(user) == unicode):
        user=user.encode("utf-8")
    try:
        test_dict[user] += 1
    except:
        test_dict[user] = 1
    final_dict[repo]= [test_dict]
        
print (test_dict)
print ("-------------------------------------------------")
print (final_dict)

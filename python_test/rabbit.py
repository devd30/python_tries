from collections import Counter
phrase="poultry outwits ants"

charac={}

# creating a dictionary
for chars in phrase:
    if chars.isspace() == False:
        j=phrase.count(chars)
        charac[chars]=j
        #total_chars = total_chars +  j
#print (charac)
total_chars=(sum(charac.values()))

#i=0
filtered_list=[]
with open("wordlist",'r', encoding='utf-8') as file:
    for vals in file:
        if len(vals) <= total_chars:
            result=[char for char in set(vals.strip('\n')) if char not in (list(set(phrase.replace(" ",""))))]
            if not result:
                if vals not in filtered_list:
                    filtered_list.append(vals)
                    #i += 1
                    #print (vals,i)

print (len(filtered_list))
for vals in filtered_list:
    val_dict=Counter(vals)
    final_dict={key:val_dict[key] for key,values in charac.items() if val_dict[key] > charac[key]}
    if (any(final_dict)):
        filtered_list.remove(vals)

print (len(filtered_list))
#print (filtered_list) 










''''
        # for ch in line:
        #     if (ch) not in charac.keys():
        #         print (ch) 
        # #print (((ch not in charac.keys()) for ch in line),i)
        #i += 1 
                #print (line)
                #i += 1
#reading wordlist file and creating new
'''
'''
def contains(word,letters):
     #if word.find("'")!=-1:
     #    return False
    if set(letters.replace(" ","")) & set(word.replace(" ","")):
        for w in letters:
            if word.count(w)>letters.count(w):
                print ("inside count part",w)
                return False
        print ("outsifde first fasle",w)
        return True
    print ("before last false")
    return False

def containAll(str,set):#str,set
    return 0 not in [c in str for c in set]
     
a=phrase.replace(" ","")
'''
        

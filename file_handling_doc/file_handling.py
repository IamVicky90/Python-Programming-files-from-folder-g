with open ('file.txt','w') as f:
    f.write('Python ia a programming language')

with open ('file.txt','a') as f:
    f.write('\nWaqas is a good programmer')
with open('file.txt','r') as f:
    output=f.read()
print(output)
############Doing the same thing with breavity##############
with open('file1.txt','w+') as f:
    f.write('This is file number 2')
    f.write('\nThis is also a file number 2')
    f.seek(0)
    r=f.read()
print(r)
###########with r+ mode##########################
with open('file1.txt','r+') as f:
    f.write('This is changing from r+ mode in file 2')
    f.write('\nThis is also a changing from from file number 2')
    f.seek(0)
    r=f.read()
############################Extract links from html file to links.txt#######
with open('test.html','r') as fr:
    with open('links.txt','a') as fa:
        fa.write('Your links has been extracted')
        for line in fr.readlines():
            if line.find('"http'):
                
                pos=line.find('"http')
                
                pos_end=line.find('"',pos+1)
                res=line[pos:pos_end]
                for i in res:
                    if i=='"':
                        i='\n'
                    fa.write(i)
#######################CSV FILES#######################################
import csv
with open('file.csv') as f:
    r=csv.reader(f)
    for content in r:
        print(content)
        
###### write csv file####

with open('file.csv','a',newline="") as f:
    write_content=csv.writer(f)
    write_content.writerow(['waqas bilal 1','2020','Pakistan'])

########################JSON FILES#############################
import json
with open('file.json','w') as f:
    json.dump({'name':'waqas','age':'20'},f)
with open('file.json','r') as f:
    contents=json.load(f)
    for key,values in contents.items():
        print(key,values)


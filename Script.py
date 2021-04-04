#Objective: Pull list of bad doamins from git get first 100 of each and put in text file
import os
def wget (url):
    location = os.getcwd()
    os.system("wget "+ url+ " -P"+location )
wget("https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts")
wget("https://raw.githubusercontent.com/Ultimate-Hosts-Blacklist/MalwareDomainList.com/master/domains.list")


#Parse The StevenBlack Host file
file1= "hosts"
file2="domains.list"

openfile = open(file1, 'r')
Lines = openfile.readlines()
count = 0
for line in Lines:
    count += 1
    if count > 39 and count < 139: #The blacklisted domains start at line 39 hence why we are ignoring lines until this point
        baddomain = line.replace('0.0.0.0','')
        print(baddomain)

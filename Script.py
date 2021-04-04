#Objective: Pull list of bad doamins from git get first 100 of each and put in text file
import os
def wget (url):
    location = os.getcwd()
    os.system("wget "+ url+ " -P"+location )
wget("https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts")

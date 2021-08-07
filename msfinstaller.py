
#!/bin/sh
# Name : MSFinstaller
# Date : 07 August, 2021
# Description : MSFinstaller is a simple python code for install Metasploit Framework Without Error.




import os
import time



def banner():           

    logo = '''
    
   \033[0;34m             ______    _______
   \033[0;34m|^\    /^|  |          |
   \033[0;34m|  \  /  |  |______    |
   \033[0;34m|   \/   |         |   |___   
   \033[0;34m|        |         |   |
   \033[0;34m|        | o ______| o |     ...INSTALLER... 
                                                              
                 \033[0;31mAuthor:devincrack\033[0;31m
                 \033[0;32mhttps://termux-hacking-pro.blogspot.com '''
    return logo
 
print(banner())

time.sleep(2)
print("Please wait, Installation is under processing.....")
os.system("unzip metasploit-framework-master.zip")
os.system("clear")
os.system("pkg update && upgrade -y")
os.system("pkg install python -y")
os.system("pkg install wget -y")
os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
os.system("chmod +x metasploit.sh")
os.system("./metasploit.sh")
time.sleep(5)
print(" The MSF is installed successfully! Type msfconsole to run the metasploit framework")

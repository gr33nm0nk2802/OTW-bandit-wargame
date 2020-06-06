#!/usr/bin/env python3

from pwn import *
import os

context.log_level = 'critical'

h="bandit.labs.overthewire.org"
u="bandit3"
p=2220
pwd=""

encoding="utf-8"

with open('flag3.txt','r') as f:
    pwd=f.read().rstrip('\n')


print("[`] Making SSH connection to \n[`] Host:",h,"\n[`] Username:",u,"at Port:",p)
try:
    
    # ssh connection done using pwntools refer documentation at (http://docs.pwntools.com/en/stable/)    
    s=ssh(host=h,user=u,password=pwd,port=p)
    print("[`] Successfully connected\n \n")
    try:
        

        print('[+] Shell has been received executing the following commands\n')
        
        print("[+] Lets see the user we are logged in as..")
        print("[#] $ whoami")
        cmd = s.process(['whoami']).recvall().decode(encoding)
        print("[#] $",cmd)
        
        print("[+] User and Group Ids")
        print("[#] $ id")
        cmd = s.process(['id']).recvall().decode(encoding)
        print("[#] $",cmd)
        
        print("[+] Files on the system along with the permission")
        print('[#] $ ls -la')
        cmd = s.process(['ls', '-la']).recvall().decode(encoding) 
        print(cmd+"\n")

        with open('flag4.txt','w') as f:
            print("[+] Writting flag to flag4.txt")
            f.write(cmd.rstrip('\n'))
            print("[+] Done\n")
            sys.exit(1)

    except:
        print("[`] Disconnected")

except:
    print("[`] Failed!!")
    print("[`] You have some error in making the SSH connection!!")
    print("[`] Please recheck the credentials ans Internet conncetion!")
    sys.exit(1)

s.close()


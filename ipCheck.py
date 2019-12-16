#!/usr/bin/python3

import subprocess
import datetime
import re 


class ipcheck():

    def ip_check(self):

        ip = input('Enter your IP address: ')
        
        #  Checking the IP address format using regular expression
        #  \d = match any digit in given string. \d{1,3} - match digits upto 3 counts only
        if not re.match(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})', ip) or any(a not in range(0,256) for a in map(int, ip.split('.'))):
                print('Invalid')
        else:
            print("This is a valid IP address")

def main():

    ipCheck = ipcheck()
    ipCheck.ip_check()

if __name__ == "__main__":
    main()

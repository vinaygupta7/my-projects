import re
from collections import Counter

def apache_log_reader(logfile):
    myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'


    with open(logfile) as f:
        log = f.read()
#        print(log)
        my_iplist = re.findall(myregex,log)
#        print my_iplist

        ipcount = Counter(my_iplist)
        print ipcount
        for k, v in ipcount.items():
            print("IP Address " + "=> " + str(k) + " " + "Count "  + "=> " + str(v))
        f.close()

if __name__ == '__main__':
    apache_log_reader("apache.logs")

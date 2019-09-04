#!/usr/bin/env python
"""
USAGE:
logparsing_apache.py apache_log_file
This script takes apache log file as an argument and then generates a report, with hostname,
bytes transferred and status
"""
import sys
def apache_output(line):
    split_line = line.split()
    return {'remote_host': split_line[0],
            'apache_status': split_line[8],
            'data_transfer': split_line[9],
    }
import re
from collections import Counter
def apache_log_reader(logfile):
    myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    with open(logfile) as f:
        log = f.read()
        my_iplist = re.findall(myregex,log)
        ipcount = Counter(my_iplist)
        for k, v in ipcount.items():
            print("IP Address " + "=> " + str(k) + " " + "Count "  + "=> " + str(v))
# Create entry point of our code

if __name__ == '__main__':
    apache_log_reader("/home/vinay/apache.logs")


def final_report(logfile):
    for line in logfile:
        line_dict = apache_output(line)
        print(line_dict)


if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print (__doc__)
        sys.exit(1)
    infile_name = sys.argv[1]
    try:
        infile = open(infile_name, 'r')
    except IOError:
        print ("You must specify a valid file to parse")
        print (__doc__)
        sys.exit(1)
    log_report = final_report(infile)
    print (log_report)
    infile.close()
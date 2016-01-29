#!/usr/bin/python

import sys
import os
from tld import get_tld

from scans import *

def driver():
        try:
            url = sys.argv[1]
            file_path = sys.argv[2]
        except:
            print "Usage: python driver.py url output_path"
            print "Example: python driver.py http://www.google.com outfile.txt"
            sys.exit()

	url_tld = get_tld(url)

	# run scans
	url_ip = get_ip(url_tld)
	robots = get_robots(url)
	whois = get_whois(url_tld)

	# output data
	data = "Url IPs:\n" + str(url_ip) + \
		"Url's whois file:\n" + str(whois) + \
		"Url's robots.txt file:\n" + str(robots)
		
	write_file(data, file_path)


def write_file(data, file_path):
	f = open(file_path, 'a')
	f.write(data)
	f.close()


if __name__ == "__main__":
	driver()

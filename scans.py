import os
import socket
import nmap
import urllib2

def get_ip(url):
	cmd = 'host ' + url
	proc = os.popen(cmd)
	data = proc.read()

	return data

def run_portscan(options, ips):
	scan_results = list()
	nm = nmap.PortScan()

	for host in ips:
		scan_results.append(nm.scan(host))

	return str(scan_results)

def get_robots(url):
	if url.endswith('/'):
		path = url
	else:
		path = url + '/'

	req = urllib2.urlopen(path + 'robots.txt', data=None)

	return req.read()

def get_whois(url_tld):
	cmd = 'whois ' + url_tld
	proc = os.popen(cmd)
	data = proc.read()

	return data
# -*- coding: UTF-8 -*-
import re
import sys
# import filter
import whois
import os, errno

def appendWrite(filename,data):
	f = open(filename,"a")
	f.write(data)
	f.close
def safeRemove(filename):
	try:
		os.remove(filename)
	except OSError as e:
		print e

def dnslist(inputFilteName,domainName):
	f = open(inputFilteName)
	d = []
	for line in f:
		if "A " and "DNS" in line :
			try:
				if line.split(",")[6].split(" ")[4] == 'A' :
					dns = line.split(",")[6].split(" ")[5].replace("\"","")
					d.append(dns)
					# print datetime+"+++"+dns
			except:
				print line
	uniqDns = set(d)
	for u in uniqDns:
		appendWrite(domainName,u)
	f.close
	return uniqDns

def whiteList(uniqDns,whiteListFilter):
	result = []
	alexa = open('PythonEvulationEntropyCode/alexa-1m.txt').read().split("\n")
	for dns in uniqDns:
		if dns.strip() not in alexa:
			appendWrite(whiteListFilter,dns)
			result.append(dns)
	return result

def queryWhois(whitelist,queryWhois_Path):
	for line in whitelist:
# 		print line
		dns = line.strip('\r\n')
		result ={}
		result['input_domain']=dns
		try:
# 			print line
			w = whois.whois(dns)
			result['creation_date']=w.creation_date[0].isoformat()
			result['domain_name']=w.domain_name
			result['name_servers']=w.name_servers
			result['registrar']=w.registrar
			result['whois_server']=w.whois_server
			result['status'] = 1
		except:
			result['status'] = 0
	    	print '--fail--'
		appendWrite(queryWhois_Path,str(result)+"\n")
# 		appendWrite(filename,data)

if __name__ == "__main__":
	# inputFilteName = "tran.csv"
	inputFilteName = sys.argv[1]
	domainName_Path = "domainName.txt"
	whiteListFilter_Path = "whiteListFilter.txt"
	queryWhois_Path = "queryWhois.txt"
	safeRemove(domainName_Path)	#檔案刪除
	safeRemove(whiteListFilter_Path)	#檔案刪除
	safeRemove(queryWhois_Path)	#檔案刪除
	uniqDns = dnslist(inputFilteName,domainName_Path)
	whitelist = whiteList(uniqDns,whiteListFilter_Path)
	queryWhois(whitelist,queryWhois_Path)
	print '++finish++'





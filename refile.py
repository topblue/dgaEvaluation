# -*- coding: UTF-8 -*-
import re
import sys

def appendWrite(filename,data):
	f = open(filename,"a")
	f.write(data)
	f.close
#sys.argv[1]
	
if __name__ == "__main__":
	twoCategory = "twoCategory.txt"
	domainName = "domainName.txt"
	f = open(sys.argv[1])
	d = []
	for line in f:
#		print line
		if "A " and "DNS" in line:
#			print line
			try:
				data =line.split(",")[0] +","+ line.split(",")[6].split(" ")[5] 
	#			data = line
				print data
				data = data[0:-1]
				appendWrite(twoCategory,data+"\n")
				d.append(line.split(",")[6].split(" ")[5])
			except:
				print line
	dd =set(d)
	for line in dd:
		line = line[0:-1]
		appendWrite(domainName,line+"\n")
	f.close

	
	
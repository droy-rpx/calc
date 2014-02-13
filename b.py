#! /usr/bin/python
import re

line = raw_input("input numbers : ")
#line = line.rstrip()
line = line.replace('\\n','')
line = line.replace('\\','')
line = line.replace('/','')
line = line.replace(' ','')
line = line.replace(';',',')
vals = line.split(',')
total = 0
no_flag = False
if bool(vals[0]):
	for val in vals:
		match = re.search("^-{0,1}\d+$", val)
		if bool(match) == False:
			print "Only numbers can be calulated"
			break
		try:
			if int(val) < 0:
                                no_flag = True
				raise ;
		except :
			print "negatives not allowed " + val
			
		if no_flag == False:
			total += int(val) 
	else:
		if no_flag == False:
			print "Total = %d" % total
		else:
			# print "Total = %d" % total
			pass
else:
	print "No numbers supplied!"

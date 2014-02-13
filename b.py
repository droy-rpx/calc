#! /usr/bin/python

line = raw_input("input numbers : ")
#line = line.rstrip()
line = line.replace('\\n','')
line = line.replace('\\','')
line = line.replace('/','')
line = line.replace(' ','')
line = line.replace(';',',')
vals = line.split(',')
total = 0
if bool(vals[0]):
	for val in vals:
		total += int(val) 
	else:
		print "Total = %d" % total
else:
	print "No numbers supplied!"

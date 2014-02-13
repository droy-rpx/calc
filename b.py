#! /usr/bin/python

line = raw_input("input numbers : ")
vals = line.split('\n')
total = 0
if bool(vals[0]):
	for val in vals:
		nums = val.split(',')
                print nums
		for num in nums:
			total += int(num) 
                	print "num = %s" % num

print "Total = %d" % total

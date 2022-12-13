#!/usr/bin/env python3
import re

hfile = open('input4.txt')
newline = '71-89,66-70'

linecount = 0
count = 0
count1 = 0
for line in hfile :
	linecount = linecount + 1
	line = line.rstrip()
	numlist = re.split(',|-',line) # multiple delimiters
	print(numlist)

# a1 always bigger or equal than a2
# b1 always bigger or equal than b2

	a1 = int(numlist[0])
	a2 = int(numlist[1])
	b1 = int(numlist[2])
	b2 = int(numlist[3])

	if (a1 < b1) and (a2 >= b1) :
		#print("b is inside a")
		count = count + 1
	elif (b1 < a1) and (b2 >= a1) :
		#print("a is inside b")
		count = count + 1
	#elif (a1 == b1) and (a2 == b2) :
	#	print("they are identical!!!")
	#	count1 = count1 + 1
	elif (a1 == b1) or (a2 == b2) :
		count = count + 1
print("number of overlaps is", count)

print(linecount)
print(count1)
exit()


errorlist = list()

for line in hfile :
	print("############NEWLINE#############")
	line = line.rstrip()
	print(line)
	linelist = list(line)

#	print(linelist)
	print(len(linelist))
	half = int(len(linelist)/2)
	tot = int(len(linelist))
	print(half, tot)


	break_out_flag = False
	for i in range(0, half) :
#		print('i=', linelist[i])
		for j in range(half, tot) :
#			print('j=', linelist[j], end = " ")
			if linelist[i] == linelist[j] :
				break_out_flag = True
				let = linelist[i]
				break
		if  break_out_flag :
			break
	errorlist.append(let)

print(errorlist)


#print(letterkey("l"))
sume = 0
for m in errorlist :
	sume = sume + int(letterkey(m))

print("total sum", sume)

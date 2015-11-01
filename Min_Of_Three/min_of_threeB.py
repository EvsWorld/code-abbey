import sys

list_of_lists = []
#Loops through standard input
for line in sys.stdin:
	#Creates a new list for each line of standard input, then loops
	#through each element (elem) in each line. Adds commas btwn elems.
	new_list = [int(elem) for elem in line.split()]

	#Appends each new_list to list_of_lists.
	list_of_lists.append(new_list)
print list_of_lists

#min_list = []
#for li in list_of_lists:
#	if li[0] < li[1] and li[0] < li[2]:
#		min_list.append(li[0])
#	elif li[1] < li[0] and li[1] < li[2]:
#		min_list.append(li[1])
#	elif li[2] < li[0] and li[2] < li[1]:
#		min_list.append(li[2])
#	else:
#		print 'Elements equal'
li = []
minm = li[0]
for li in list_of_lists:
	if minm > li[1]:
		minm = li[1]
	if minm > li[2]:
		minm = li[2]
	min_list.append(minm)






print 'min_list = %r' % min_list

#loops back through min_list converting each int to string, then \
#joins the list (removes commas), and prints all values
print 'min_list = %r' % " ".join(str(x) for x in min_list)

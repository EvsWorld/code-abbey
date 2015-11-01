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

min_list = []
for li in list_of_lists:
	if li[0] < li[1]:
		min_list.append(li[0])
	elif li[0] > li[1]:
		min_list.append(li[1])
	else:
		print 'Elements equal'
print 'min_list = %r' % min_list

#loops back through min_list converting each int to string, then \
#joins the list (removes commas), and prints all values
print 'min_list = %r' % " ".join(str(x) for x in min_list)





#	outer.append(ready)
#ready_list = input_nums.split()  #Uses .split() to make a comma seper
#print ready_list



"""Goes through ready list and adds the value of each number in \
ready_list to the value 'sum'"""
#sum = 0
#for i in ready_list:

#	sum += int(i)
#	print (sum,i)

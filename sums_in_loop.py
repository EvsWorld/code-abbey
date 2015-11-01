import sys

list_of_lists = []
#Loops through standard input
for line in sys.stdin:
	#Creates a new list for each line of standard input, then loops
	#through each element (elem) in each line. Adds commas btwn elems.
	new_list = [int(elem) for elem in line.split()]
	#Sums each input line (new_list) & appends each to list_of_lists.
	list_of_lists.append(sum(new_list))

#loops back through list_of_lists converting each int to string, then \
#joins the list (removes commas), and prints all jalues
print " ".join(str(x) for x in list_of_lists)





#	outer.append(ready)
#ready_list = input_nums.split()  #Uses .split() to make a comma seper
#print ready_list



"""Goes through ready list and adds the value of each number in \
ready_list to the value 'sum'"""
#sum = 0
#for i in ready_list:

#	sum += int(i)
#	print (sum,i)

from sys import argv

#list_length = input('Input how many numbers you will input:')

'''Assigns input_nums to arguments passed in at command line'''
script, input_nums = argv

#input_nums = input('Input a string, consisting of numbers seperated by spaces:')
print input_nums

'''Takes each number in string, changes it to int, then appends it into ready_list'''
#ready_list = []
#for s in input_nums:
#	ready_list.append(int(s))	   
								  
	
ready_list = input_nums.split()  #Uses .split() to make a comma seperated list
print ready_list



"""Goes through ready list and adds the value of each number in \
ready_list to the value 'sum'"""
sum = 0
for i in ready_list:   

	sum += int(i)
	print (sum,i)
	
	
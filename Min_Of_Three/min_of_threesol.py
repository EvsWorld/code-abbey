import sys

#split_data = sys.stdin.split()
#print split_data
minimums = []

for line in sys.stdin:
	split_data = [int(elem) for elem in line.split()]

	a = int(split_data.pop())
	b = int(split_data.pop())
	c = int(split_data.pop())

	if a < b:
		b = a
	if b < c:
		c = b
	minimums.append(int(c))
print 'minimums = %r' % " ".join(str(x) for x in minimums)





#print 'min_list = %r' % min_list

#loops back through min_list converting each int to string, then \
#joins the list (removes commas), and prints all values
#print 'min_list = %r' % " ".join(str(x) for x in min_list)

import sys

#split_data = sys.stdin.split()
#print split_data
minimum = 0
maximum = 0
data = sys.stdin.readline()

for elem in data.split():
	int(elem)
	if int(elem) < minimum:
		minimum = int(elem)
	if int(elem) > maximum:
		maximum = int(elem)

print 'minimum = %r, maximum = %r' % (minimum, maximum)



# Terminal not let me input the values required for the problem.

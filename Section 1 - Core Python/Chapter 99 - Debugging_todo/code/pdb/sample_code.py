"""
    Sample file for debugging

"""


def multi_add(*argv):
	total = 0
	for a in argv:
		total = total + a 
	return total 

multi_add(10, 2, 4)

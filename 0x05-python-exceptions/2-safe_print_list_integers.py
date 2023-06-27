#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
	count = 0
	real = 0
	try:
		while count != x:
			try:
				print('{:d}'.format(my_list[count]), end='')
				real += 1
			except:
				pass
			count += 1
	except:
		None
	print()
	return real

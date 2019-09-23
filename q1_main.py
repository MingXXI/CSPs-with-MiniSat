from a3_q1 import *
import csv


def test(max):
	# with open('names.csv', 'w') as csvfile:
	# 	fieldnames = ['first_name', 'last_name']
	# 	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	# 	writer.writeheader()
	# 	writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
	# 	writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
	# 	writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})



	with open('q1.csv', 'w') as csvfile:
		fieldnames = ['N', 'Solving_Time']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		
		writer.writeheader()
		t = []
		size = []
		cur_time = 0
		for i in range(140,max+1):
			make_queen_sat(i)
			st = time.time()
			os.system('minisat queenSAT.txt out')
			cur_time = time.time() - st
			if cur_time < 10:
				writer.writerow({'N': i, 'Solving_Time': cur_time})
			else:
				break

test(150)
import math
import time
import csv
import os

def make_queen_sat(N):
	f=open('queenSAT.txt','w+')
	f.truncate(0)
    	# refer to: https://blog.csdn.net/yinghuo110/article/details/79179165
    	# refer to: https://www.cnblogs.com/wushuaishuai/p/8511606.html
	if N == 0:
		print('p cnf', N*N, '0', file = f)
		f.close()
		return
	if N == 1:
		print('p cnf', N*N, '1', file = f)
		f.close()
		return

	print('p cnf', N*N, 'what', file = f)
	count = 0

	# row constrains ---------
	for i in range (0, (N*N-N+1), N):
		for j in range(i, i+N):
			for k in range(j+1, i+N):
				print(-(j+1), -(k+1), 0, file = f)
				count += 1

	# Unique in rows -----*-----
	if N>1:
		for i in range (0, (N*N-N+1), N):
			print(i+1, file = f, end = " ")
			for j in range(i+1, i+N):
				print(j+1, file = f, end = " ")
			print(0, file = f)
			count += 1

	# column constrains |||||||||||||
	for i in range(0, N):
		for j in range(i, N*N, N):
			for k in range(j+N, N*N, N):
				print(-(j+1), -(k+1), 0, file = f)
				count += 1

	# Unique in column ||||*||||
	for i in range(0,N):
		print(i+1, file = f, end = " ")
		for j in range(i+N, N*N, N):
			print(j+1, file = f, end = " ")
		print(0, file = f)
		count += 1
	# diagonal \\\\\\\\
	N_square = N*N
	for i in range(N_square,N,-N):
		for j in range(i,0,-N-1):
			for k in range(j-N-1,0,-N-1):
				count+=1
				print(-(k),-(j),0, file = f)

	for i in range(1+N,N_square,N):
		for j in range(i,N_square,N+1):
			for k in range(j+N+1,N_square,N+1):
				count+=1
				print(-(j),-(k),0, file = f)

	for i in range(N_square-N+1,1,-N):
		for j in range(i,1,-N+1):
			for k in range(j-N+1,1,-N+1):
				count+=1
				print(-(k),-(j),0, file = f)

	for i in range(2*N,N_square,N):
		for j in range(i,N_square,N-1):
			for k in range(j+N-1,N_square,N-1):
				count+=1
				print(-(j),-(k),0, file = f)

	f.close()

	with open('queenSAT.txt', 'r') as f:
		line = f.readlines()
	line[0] = line[0].replace("what", "%d" %count)
		# refer to: https://www.cnblogs.com/wangjq19920210/p/10143575.html
		# && https://www.cnblogs.com/linkenpark/p/5167867.html

	with open('queenSAT.txt', 'w') as fout:
		fout.writelines(line)
	fout.close()
	f.close()
	return


def draw_queen_sat_sol(sol):
	if sol[0]=="U":
		print("No Solution")
		return
	list = [int(x) for x in sol.split()]
	if len(list) > 1601:
		print("Too Big! N must be less than 40")
		return
	N = int(math.sqrt(len(list) - 1))
	index = 0
	for i in range(N):   
		for j in range(N):
			if list[index]>0:
				print("Q ", end = "")
			else:
				print("* ", end = "")
			index += 1
		print("")
	return  

# def draw_queen_sat_sol(sol):
# 	file = open(sol, "r")
# 	if file.mode == "r":
# 		line = file.readlines()
# 		# refer to: https://www.cnblogs.com/xiugeng/p/8635862.html
# 		if line[0] == "UNSAT\n":
# 			print("NO SOLUTION")
# 			return
# 		list = [int(x) for x in line[1].split()]
# 		if len(list) > 1601:
# 			print("Too Big! N must be less than 40")
# 			return
# 		N = int(math.sqrt(len(list) - 1))
# 		index = 0
# 		for i in range(N):
# 			for j in range(N):
# 				if list[index]>0:
# 					print("Q ", end = "")
# 				else:
# 					print("* ", end = "")
# 				index += 1
# 			print("")
# 	return



def test():
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
		## refer to: https://docs.python.org/2/library/csv.html
		
		writer.writeheader()
		i = 2
		t = []
		size = []
		cur_time = 0
		while 1: 
			make_queen_sat(i)
			st = time.time()
			os.system('minisat queenSAT.txt out')
			cur_time = time.time() - st
			print('running time', cur_time)
			if cur_time < 10:
				writer.writerow({'N': i, 'Solving_Time': cur_time})
				i+=1
			else:
				break
if __name__=="__main__":
	test()

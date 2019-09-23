import numpy as np
import csv
import random
import os
import time
import math
import signal

def myHandler(signum, frame):
    print("Time Out!")
    exit()




def rand_graph(n,p):
    a = []
    b = []
    for i in range(n):
        a.append(i) 
        b.append([])
    graph = dict(zip(a,b))
    for i in range (n):
        j = i+1
        while j < n:
            if random.random() <= p:
                graph[i].append(j)
                graph[j].append(i)
            j += 1
    return graph

def make_ice_breaker_sat(graph, k):
    count = 0
    graph_length = len(graph)
    for i in range(graph_length):
        count += len(graph[i])
    count = int(count/2)
    string = "p cnf " + str(graph_length*k) + ' ' + str(int((k-1)*k/2 + 1)*graph_length+count*k) + '\n'

    if (k<0 | graph_length==0):
        return string

    for i in range(graph_length):
        exist = ""
        for j in range(1,k+1):
            a = i*k+j
            exist += str(a) + ' '
            for l in range(j+1, k+1):
                string += str(-a) + ' ' + str(-(i*k+l)) + ' 0\n' ## one can be assigned to only one group
        string += exist + '0\n'     ## one should be assigned to at least one group

        for each in graph[i]:
            if each > i:
                for m in range(1, k+1):
                    string += str(-(i*k+m)) + ' ' + str(-(each*k+m)) + ' ' + '0\n' ##people who know each other can not be assigned into same group

    return string


def find_min_teams(graph):
    if len(graph) == 0:
        return 0
    i = 0
    j = len(graph)
    print(j)
    k = (i+j)//2
    while 1:
        print(i,j,k)
        if k == j:
            return k
        if k == i:
            return j
        string = make_ice_breaker_sat(graph, k)
        f = open('q2.txt', 'w+')
        f.truncate(0)
        print(string, file = f, end = '')
        f.close()
        os.system('minisat q2.txt some.out')
        f = open('some.out', 'r')
        lines = f.readlines()
        if (lines[0] == "UNSAT\n"):
            i = k
        else:
            j = k
        k = (i+j)//2
        f.close()
    return k


def main():
    # with open('names.csv', 'w') as csvfile:
    #   fieldnames = ['first_name', 'last_name']
    #   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #   writer.writeheader()
    #   writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    #   writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    #   writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
    with open ('a3_q2.csv', 'w') as csvfile:
        fieldnames = ['0.1_group', '0.1_time','0.2_group', '0.2_time','0.3_group', '0.3_time','0.4_group', '0.4_time','0.5_group', '0.5_time','0.6_group', '0.6_time','0.7_group', '0.7_time','0.8_group', '0.8_time','0.9_group', '0.9_time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        N = 16
        for p in range(1,10):
            groups = []
            time_record = []
            pos = p/10
            for i in range(10):
                a = rand_graph(N, pos)
                st = time.time()
                b = find_min_teams(a)
                time_record.append(time.time()-st)
                writer.writerow({str(pos)+'_group': b, str(pos)+'_time': time.time()-st})

    return

if __name__=="__main__":
    main()

# 0.1 120 5 5.0 0.9151407241821289
# 0.2 76 6 6.0 2.7507344484329224
# 0.3 65 7 7.0 2.434220290184021
# 0.4 44 7 7.4 8.442063117027283
# 0.5 39 9 8.2 45.2064710855484
# 0.6 32 9 8.7 52.41612284183502
# 0.7 27 10 9.5 24.912330675125123

# 0.9 17 10 9.6 11.972477054595947




















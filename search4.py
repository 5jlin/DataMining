import csv
import time
import itertools
import linecache
A = []
B = []
C = [0,0,0]
D = [0,0,0]

def choose(select,idx):
    a1 = 0
    a2 = 0
    a3 = 0
    c = 0  #for speedup

    for i in range(idx, idx+1000000):
#        print(i)   
        row2 = linecache.getline('merge_train.csv', i)
#        print(type(row2.split(",")[0]))
#        print(row2)
        if (row2.split(",")[0] == select) :
            c = 1
#            print(row2.split(",")[8])
            
            if row2.split(",")[8] == "1" :

                if row2.split(",")[3] == "2015" :
                    C[0] = C[0] + 1
                    D[0] = D[0] + int(row2.split(",")[6])
                elif row2.split(",")[3] == "2014" :
                    C[1] = C[1] + 1
                    D[1] = D[1] + int(row2.split(",")[6])
                elif row2.split(",")[3] == "2013" :
                    C[2] = C[2] + 1
                    D[2] = D[2] + int(row2.split(",")[6])
                    
        if (row2.split(",")[0] != select) and (c == 1) :
            break;
                    
    a1 = D[0] / C[0]
    a2 = D[1] / C[1]
    a3 = D[2] / C[2]
    if ((abs(a2 - a1) / a2) > 0.035) or ((abs(a3 - a2) / a2) > 0.035) :
        A.append(select)
        '''
        print(D[0] / C[0])
        print(D[1] / C[1])
        print(D[2] / C[2])
        print(abs(a2 - a1) / a2)
        print(abs(a3 - a2) / a2)
        '''

start = time.time()
for x in range(1110):
     if x % 80 == 0:
          print("current: " + str(x) )
     if x == 0 :
          continue
     else :
          choose(str(x),(x-1)*900)

print(len(A))
end = time.time()
elapsed = end - start
print ("Time taken: ", elapsed, "seconds.")


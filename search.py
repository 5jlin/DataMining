import csv

A = []
B = []
C = [0,0,0,0,0,0,0]
D = [0,0,0,0,0,0,0]


def choose(select):
     with open('store.csv') as f:
          f_csv = csv.reader(f)
          headers = next(f_csv)
          for row in f_csv:
               if row[2] == select :
                    A.append(row[0])
          f.close()
     with open('train.csv') as f2:
          f_csv = csv.reader(f2)
          headers = next(f_csv)
          for row2 in f_csv:
               if row2[0] in A :
                    if row2[5] == '1':
                         if row2[1] == '1' :
                              C[0] = C[0] + 1
                              D[0] = D[0] + int(row2[3])
                         elif row2[1] == '2' :
                              C[1] = C[1] + 1
                              D[1] = D[1] + int(row2[3])
                         elif row2[1] == '3' :
                              C[2] = C[2] + 1
                              D[2] = D[2] + int(row2[3])
                         elif row2[1] == '4' :
                              C[3] = C[3] + 1
                              D[3] = D[3] + int(row2[3])
                         elif row2[1] == '5' :
                              C[4] = C[4] + 1
                              D[4] = D[4] + int(row2[3])
                         elif row2[1] == '6' :
                              C[5] = C[5] + 1
                              D[5] = D[5] + int(row2[3])
                         elif row2[1] == '7' :
                              C[6] = C[6] + 1
                              D[6] = D[6] + int(row2[3])
          f2.close()
          print("Assortment is "+select)
          print(C)
          print(D)
          print(D[0] / C[0])
          print(D[1] / C[1])
          print(D[2] / C[2])
          print(D[3] / C[3])
          print(D[4] / C[4])
          print(D[5] / C[5])
          print(D[6] / C[6])

choose('a')
choose('b')
choose('c')




'''

with open('store.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        if row[1] == 'a' :
            A.append(row[0])
    #        print (row)
    f.close()

with open('train.csv') as f2:
    f_csv = csv.reader(f2)
    headers = next(f_csv)
    for row2 in f_csv:
#        if row2[0] in A :
#            B.append(row2)
         #   print (row2[0])
         if row2[5] == '1':
            if row2[1] == '1' :
                C[0] = C[0] + 1
                D[0] = D[0] + int(row2[3])
            elif row2[1] == '2' :
                C[1] = C[1] + 1
                D[1] = D[1] + int(row2[3])
            elif row2[1] == '3' :
                C[2] = C[2] + 1
                D[2] = D[2] + int(row2[3])
            elif row2[1] == '4' :
                C[3] = C[3] + 1
                D[3] = D[3] + int(row2[3])
            elif row2[1] == '5' :
                C[4] = C[4] + 1
                D[4] = D[4] + int(row2[3])
            elif row2[1] == '6' :
                C[5] = C[5] + 1
                D[5] = D[5] + int(row2[3])
            elif row2[1] == '7' :
                C[6] = C[6] + 1
                D[6] = D[6] + int(row2[3])
    f2.close()
print(C)
print(D)
print(D[0] / C[0])
print(D[1] / C[1])
print(D[2] / C[2])
print(D[3] / C[3])
print(D[4] / C[4])
print(D[5] / C[5])
print(D[6] / C[6])
'''

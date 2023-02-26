

import re
import numpy as np
from itertools import combinations
from decimal import Decimal
import copy
import datetime
starttime = datetime.datetime.now()
orb = []#Define ORB
ls = []
l1 = []
l = []

def delete_first_lines(file, count1,count2):
    fin = open(file, 'r')
    a = fin.readlines()
    fout = open(file, 'w')
    b = ''.join(a[count1:count2])
    fout.write(b)
filepath0="C:\\Users\\dell\\Desktop\\"
filename0="n=7" 
file0 = filepath0 + filename0 + ".txt"
count1=0
count2=75
delete_first_lines(file0, count1,count2)
for line in open(file0,"r"): #Set the file object and read each line of file     
     point=[float(s) for s in re.findall(r'-?\d+\.\d*', line)] #Regular expression recognition of floating point numbers
     del point[-3:]#cut z axis
     orb.append(point)


for i in range(1,8):
    for j in range(31):
        if (i*4 - j) == -2:
            ls.append([i,j])            
ls.append([8,32])
for i in range(9,14):
    for j in range(44):
        if (i*2 - j) == -17:
            ls.append([i,j])
ls.append([14,45])
for i in range(15,19):
    for j in range(55):
        if (i*2 - j) == -18:
            ls.append([i,j])
ls.append([19,56])
for i in range(20,23):
    for j in range(64):
        if (i*2 - j) == -19:
            ls.append([i,j])
ls.append([23,65])
for i in range(24,26):
    for j in range(71):
        if (i*2 - j) == -20:
            ls.append([i,j])
for i in range(26,28):
    for j in range(76):
         if (i*3 - j) == 6:
            ls.append([i,j]) 


c0 = np.abs(orb[1][1]-orb[0][1])#键长

for i in range(len(ls)):
    a = ls[i][1]
    x = orb[a-1][0]
    y2 = orb[a-1][1]
    y = y2 - c0
    l1.append([x,y])



l2 = []

for i in range(len(l1)):
    x1 = l1[i][0] - (np.sqrt(3))*c0/2 
    x10 = eval(str(Decimal(x1).quantize(Decimal("0.1"), rounding = "ROUND_HALF_UP")))
    y1 = l1[i][1] + 1*c0/2
    y10 = eval(str(Decimal(y1).quantize(Decimal("0.1"), rounding = "ROUND_HALF_UP")))   
    x2 = l1[i][0] - (np.sqrt(3))*c0/2 
    x20 = eval(str(Decimal(x2).quantize(Decimal("0.1"), rounding = "ROUND_HALF_UP")))
    y2 = l1[i][1] - 1*c0/2
    y20 = eval(str(Decimal(y2).quantize(Decimal("0.1"), rounding = "ROUND_HALF_UP")))
    x3 = l1[i][0] 
    x30 = eval(str(Decimal(x3).quantize(Decimal("0.1"), rounding = "ROUND_HALF_UP")))
    y3 = l1[i][1] - c0
    y30 = eval(str(Decimal(y3).quantize(Decimal("0.1"), rounding = "ROUND_HALF_UP")))
    x4 = l1[i][0] + (np.sqrt(3))*c0/2 
    x40 = eval(str(Decimal(x4).quantize(Decimal("0.1"), rounding = "ROUND_HALF_UP"))) 
    y4 = l1[i][1] - 1*c0/2
    y40 = eval(str(Decimal(y4).quantize(Decimal("0.1"), rounding = "ROUND_HALF_UP")))
    x5 = l1[i][0] + (np.sqrt(3))*c0/2 
    x50 = eval(str(Decimal(x5).quantize(Decimal("0.1"), rounding = "ROUND_HALF_UP")))
    y5 = l1[i][1] + 1*c0/2
    y50 = eval(str(Decimal(y5).quantize(Decimal("0.1"), rounding = "ROUND_HALF_UP")))
    x6 = l1[i][0] 
    x60 = eval(str(Decimal(x6).quantize(Decimal("0.1"), rounding = "ROUND_HALF_UP")))
    y6 = l1[i][1] + c0
    y60 = eval(str(Decimal(y6).quantize(Decimal("0.1"), rounding = "ROUND_HALF_UP")))
    l2.append([[x10,y10],[x20,y20],[x30,y30],[x40,y40],[x50,y50],[x60,y60]])


l11 = []
l22 = []
l222 = []
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
c = list(combinations(b,7))



doc = open("C:\\Users\\dell\\Desktop\\7-排列组合.txt",'w') 
for i in range(len(c)):

    x1 = c[i][0]
    #print(x1)
    x2 = c[i][1]
    #print(x2)
    x3 = c[i][2]
    x4 = c[i][3] 
    x5 = c[i][4]
    x6 = c[i][5]
    x7 = c[i][6]
    #print(c[i])
    for j in range(6):
      l11.append(l2[(x1-1)][j])#
    for j in range(6):
      l11.append(l2[(x2-1)][j])#
    for j in range(6):
      l11.append(l2[(x3-1)][j])#
    for j in range(6):
      l11.append(l2[(x4-1)][j])#
    for j in range(6):
      l11.append(l2[(x5-1)][j])#
    for j in range(6):
      l11.append(l2[(x6-1)][j])#
    for j in range(6):
      l11.append(l2[(x7-1)][j])#

    z1 = 0
    for m1 in range(len(c[i])):
        l110 = copy.copy(l11)
        del l110[6*m1:6*m1+6]
        l = c[i][m1]
        l22 = []
        for n1 in range(6):
          l22.append(l2[(l-1)][n1])
       
        y1 = 0
        for k1 in range(len(l22)):
       
           if l22[k1] in l110:
            y1 = y1+1
        if y1 >=1:
          z1 = z1+1    

    if z1 >= 7:

      c0 = list(combinations(c[i],2))
 
      z2 = 0
      for ii in range(len(c0)):
        l1100 = copy.copy(l11)
        n1 = c0[ii][0]
        n2 = c0[ii][1]
        l222 = []
        for j in range(6):
           l222.append(l2[(n1-1)][j])
        for j in range(6):
           l222.append(l2[(n2-1)][j])
        for x in l222:
          if x in l1100:
             l1100.remove(x)
 
        y2 = 0
        for k2 in range(len(l222)):
        #print(k2)     
           if l222[k2] in l1100:
            #print(l222[k2])  
             y2 = y2+1
           #print(y2)
        if y2 >=1:
          z2 = z2+1
        del l222[:]
    if z2 >= len(c0) and z1 >= 7:  

      c00 = list(combinations(c[i],3))

      z3 = 0
      for iii in range(len(c00)):
        l11000 = copy.copy(l11)
        n1 = c00[iii][0]
        n2 = c00[iii][1]
        n3 = c00[iii][2]
        l2222 = []
        for j in range(6):
           l2222.append(l2[(n1-1)][j])
        for j in range(6):
           l2222.append(l2[(n2-1)][j])
        for j in range(6):
           l2222.append(l2[(n3-1)][j])
        for x in l2222:
          if x in l11000:
             l11000.remove(x)
 
        y3 = 0
        for k3 in range(len(l2222)):
        #print(k3)     
           if l2222[k3] in l11000:
            #print(l2222[k3])  
             y3 = y3+1
        if y3 >=1:
          z3 = z3+1
        del l2222[:]
       
    if z3 >= len(c00) and z2 >= len(c0) and z1 >= 7:    
     
        doc.write('%s'%x1+' '+'%s'%x2+' '+'%s'%x3+' '+'%s'%x4+' '+'%s'%x5+' '+'%s'%x6+' '+'%s'%x7+'\n')
    del l11[:]
    del l22[:]
doc.close()
endtime = datetime.datetime.now()
print (endtime - starttime)


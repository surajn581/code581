from numpy import binary_repr as binary
from collections import deque as dd
import math as mm
import time as t

def bin_add(*args): return bin(sum(int(x, 2) for x in args))[2:]

comments = ['shift right','A<-A-M','A<-A+M']
comment=0
seperatorline='---'*18

list=[]
list.append(input("enter number"))
list.append(input("enter number"))

M=max(list)
Q=min(list)

if M<0:
    width=int(mm.log(-M)/mm.log(2))+1+1
else:
    width=int(mm.log(M)/mm.log(2))+1+1

listt=[]
Mbinary=binary(M,width)
Qbinary=binary(Q,width)
negMbinary=binary(-M,width)
A=binary(0,width)
Q1='0'
count=width
print "M= ",M," Mbinary= ",Mbinary," -M=",negMbinary
print "Q= ",Q," Qbinary= ",Qbinary

def rotate():
    global A;global Qbinary;global Q1;global count
    valuelist=[]
    value=dd(A+Qbinary+Q1)
    temp=value[0]
    value.rotate()
    value[0]=temp
    #conveting deque to list
    for obj in value:
        valuelist.append(obj)
    A=''.join(valuelist[0:width])
    Qbinary=''.join(valuelist[width:(2*width)])
    Q1=valuelist[-1]    
    count=count-1
    if count>=0:
        print A," ",Qbinary," ",Q1," ",Mbinary," ",count,"    ",comments[0]
        print seperatorline


def Answer(binary1):
    listbit=[]
    if binary1[0]=='0':
        return int(binary1,2)
    else:
        seq=dd(binary1)
        for bit in seq:
            listbit.append(str(int(bit)^1))
        binary1=''.join(listbit)
        binary1=int(binary1,2)+1
        return -1*binary1
    

print" ","A"," "*(width-1),"Q"," "*(width-1),"Q1"," "*(width/2),"M"," "*(width/4),"Count"," "*(width/4),"Comment"
print A," ",Qbinary," ",Q1," ",Mbinary," ",count,"    ","initialize"
print seperatorline
while count>0:
    
    if Qbinary[-1]==Q1: rotate(); continue
    elif count>0:
        if Q1=='0': A=bin_add(A,negMbinary); comment=1
        else: A=bin_add(A,Mbinary); comment=2
        if len(A)>width:
                t=dd(A)
                
                for digits in t:                    # converting deque to list
                    listt.append(digits)
                    
                A=''.join(listt[1:])
        print A," ",Qbinary," ",Q1," ",Mbinary," "," ","    ",comments[comment]
        listt=[]
        rotate()
        continue


answerbinary=A+Qbinary
answer=Answer(answerbinary)
print M," * ",Q," = ",answerbinary," = ",answer
        
    


from numpy import binary_repr as binary
from collections import deque as dd
import math as mm
import time as t

#function to get binary addition
def bin_add(*args): return bin(sum(int(x, 2) for x in args))[2:]

#all comments in one place
comments = ['shift right','A<-A-M','A<-A+M']
comment=0
seperatorline='---'*18

#input two values
list=[]
list.append(input("enter number"))
list.append(input("enter number"))

M=max(list)
Q=min(list)

#to get the length of the binary value (number of bits), this will help in printing with proper spaces.
#as well as to get the minimum number to bits to represent both numbers in binary
if M<0:
    width=int(mm.log(-M)/mm.log(2))+1+1
else:
    width=int(mm.log(M)/mm.log(2))+1+1

listt=[]
#binary() is a numpy method, here witdth indicates the no. of bits the binary representation of the number will have
Mbinary=binary(M,width)
Qbinary=binary(Q,width)
negMbinary=binary(-M,width)
A=binary(0,width)
Q1='0'

#initializing count as the number of bits
count=width
print "M= ",M," Mbinary= ",Mbinary," -M=",negMbinary
print "Q= ",Q," Qbinary= ",Qbinary

def rotate():
    '''function to rotate A-Q-Q1'''
    
    #this function takes A-Q-Q1 as a deque object since rotating is simpler with deque, but since deques can't be sliced(as far as I know)
    #the deque is then converted to a list by iterating over the deque and then the slicing is performed
    #the print statements have also been added here for simplicity
    
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
    '''function to convert binary value to decimal value'''
    listbit=[]
    
    #check if the binary number if non-negative, if yes then return the decimal value
    if binary1[0]=='0':
        return int(binary1,2)
    
    #getting 2's complement of if the number is negative
    else:
        #binary number is stored in a deque object
        
        seq=dd(binary1)
        
        #iterating over the deque object while EX-OR-ing each bit with 1 ('^' is EX-OR)
        #0 ^ 1 = 1 and 1 ^ 1 = 0, so it's basiclly just inverting the bit value
        
        for bit in seq:
            listbit.append(str(int(bit)^1))
        binary1=''.join(listbit)
        binary1=int(binary1,2)+1
        return -1*binary1
    
#I didn't knew a more elegant method to print all the data so bear with this part
#as mentiond in line 22, the width information comes handy while printing with proper spaces

print" ","A"," "*(width-1),"Q"," "*(width-1),"Q1"," "*(width/2),"M"," "*(width/4),"Count"," "*(width/4),"Comment"
print A," ",Qbinary," ",Q1," ",Mbinary," ",count,"    ","initialize"
print seperatorline

#count is set to count=width initially and keeps decrementing by 1 after each rotation

while count>0:
    
    if Qbinary[-1]==Q1: rotate(); continue
    elif count>0:
        #this is just booths algorithm written in python, comment is the index of the appropriate comment from the list comments
        #see line 10
        
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
        
    


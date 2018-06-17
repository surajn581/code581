def compare(work,need):
    '''function to compare each value of work with each value of need at same index'''
    for k in range(len(work)):
        if work[k]<need[k]:
            return False
    return True

def add(work,allocation):
    '''function to add each value of work to each value of allocation by index'''
    for k in range(len(work)):
        work[k]=work[k]+allocation[k]

#input number of processes and no. of resources
n=int(input('enter the number of processes'))
m=int(input('enter the number of resources'))

#I know I could've done this in a single line but I didn't know then.
allocationbuffer=[];maxbuffer=[];needbuffer=[]
allocation=[];maximum=[];need=[]
available=[]; work=[];safesequence=[];

finish=[0 for i in range(n)] 

#I've used this method to input into multidimensional list because I didn't know any other way

for process in range(n):
    allocationbuffer=[];maxbuffer=[];needbuffer=[]
    print 'for process ',process,' :'
    for resource in range(m):
        allocationbuffer.append(int(input('enter allocation')))
    for resource in range(m):
        maxbuffer.append(int(input('enter max')))
    for i in range(m):
        needbuffer.append(maxbuffer[i]-allocationbuffer[i])
        
    allocation.append(allocationbuffer)
    maximum.append(maxbuffer)
    need.append(needbuffer)
    
for i in range(m):
    available.append(int(input('enter available')))
print available

#printing in a tabular format, here I'm using the number of resources(m) to calculate appropriate spacing
print 'allocation\tmaximum\t\tneed'
for process in range(n):
    print allocation[process],'\t'*(4/m),maximum[process],'\t'*(4/m),need[process]

work=available
print 'work: ',work

#Running the loop utill all processes have been finished
while 0 in finish:
    condition =True
    for i in range(n):                
        if compare(work,need[i]) and finish[i]==0:
            add(work,allocation[i])
            finish[i]=max(finish)+1

print 'finishing order: ',finish

#calculating the sequence in which the process got finished
for i in range(1,max(finish)+1):
    safesequence.append(finish.index(i))

print 'safe sequence : ',safesequence
    
    
    

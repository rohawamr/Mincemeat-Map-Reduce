from __future__ import division
import mincemeat
import sys
import math

f=open(sys.argv[1],'r')
cs=list(f)
f.close()

data=[]
temp=[]
totsum=0

c=0
for l in cs:
   c+=1
   #totsum+=int(l)
   temp.append(int(l.rstrip('\n')))
   if((c%10)==0):
       data.append(temp)
       temp=[]
data.append(temp)

l=dict(enumerate(data))


#sys.exit(0)



def mapfn(k,v):
    for w in v:
        yield 'sum',w
        #yield 'count',1
    

def reducefn(k,v):
    r1=sum(v)
    r2=len(v)
    print r2
    m=r1/r2
    std=0
    for i in range(r2):
       std+=pow(abs(v[i]-m),2)  
    res=pow((std/r2),0.5)
    return r1,r2,res

s=mincemeat.Server()
s.datasource=l
s.mapfn=mapfn
s.reducefn=reducefn

results=s.run_server(password="changeme")

reslist=[]


print '(sum,count,stddev)= ',results['sum']

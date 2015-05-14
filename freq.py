from __future__ import division
import mincemeat
import sys


f=open(sys.argv[1],'r')
cs=list(f)
f.close()


l=dict(enumerate(cs))


def mapfn(k,v):
    for w in v.split():
        w=list(w)
        for i in w:
            yield i,1
            yield 'count',1
            
            
    

def reducefn(k,v):
    res=sum(v)
    return res


s=mincemeat.Server()
s.datasource=l
s.mapfn=mapfn
s.reducefn=reducefn

results=s.run_server(password="changeme")

reslist=[]
tot=results['count']
#result=[]
#result=results[1:]
print float((10229/int(tot))*100)

print 'Total count is ',tot
for k,v in results.items():
    if k!='count':
        x=round((v/tot)*100,1)
        reslist.append((k,v,x))

reslist=sorted(reslist,key=lambda a:a[1])

print reslist

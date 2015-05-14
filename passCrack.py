#!/usr/bin/python
from __future__ import division
import mincemeat
import sys
import hashlib

#provide password as command line input
strinp = str(sys.argv[1])

#enumerate all possible words upto length of 4

def enum(length, possibles):
  ret = []
  if length == 1:
    return possibles
  else:
    subs = enum(length -1, possibles)
    for ch in possibles:
      for sub in subs:
        ret.append(str(ch) + str(sub))
  return ret

    
l=[]
    
one=[enum(1,"abcdefghijklmnopqrstuvwxyz0123456789")]
two=enum(2,"abcdefghijklmnopqrstuvwxyz0123456789")
three=enum(3,"abcdefghijklmnopqrstuvwxyz0123456789")
four=enum(4,"abcdefghijklmnopqrstuvwxyz0123456789")

l=one + two + three+ four
print len(l)

#making chunks of 1200
c=1
inp=[]
temp=[]
for i in l:
  if c%1200==0:
    temp.append(strinp)
    inp.append(temp)
    temp=[]
  c=c+1
  temp.append(i)

datasource=dict(enumerate(inp))

def mapfn(k,v):
  import hashlib
  a=v[-1]
  print a
  for w in v:
    x=hashlib.md5(w).hexdigest()
    if x[:5]==a:
      yield w,x[:5]
        
  

def reducefn(k,v):
  return v

s=mincemeat.Server()
s.datasource=datasource
s.mapfn=mapfn
s.reducefn=reducefn

results=s.run_server(password="changeme")
#print results
if results:
  print 'We have cracked the password, the list consists of',len(results),'elements' 
  print 'the list of possible values are:'
  print results  
else:
  print 'We could not crack the password'

sys.exit(0)

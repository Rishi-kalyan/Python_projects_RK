#Not optimized for large numbers, better to figure out some pattern and add calculation.
import itertools as c
n=int(input())
k='0'*(n*2)+'1'*(n*2)
l=list(set(c.permutations(k,n*2)))
c=0
for i in l:
    a=list(i)[:n]
    b=list(i)[n:]
    if a.count('1')==b.count('1') and a.count('0')==b.count('0'):
        c+=1
print(c)

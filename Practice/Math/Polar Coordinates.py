#Answer to Polar Coordinates

import cmath
n=input()
k=0
j=0
p=0
t=0
if(n[0]=='-'):
    p=1
for i in range(p,len(n)-1):
    if(n[i]!='+' and n[i]!='-' and j==0):
        k=(k*10)+int(n[i])
    if(n[i]=='+' or n[i]=='-'):
        j=1
        l=n[i]
        r=i
if(p==1):
    k*=-1
for i in range(r+1,len(n)-1):
    t=(t*10)+int(n[i])
if(l=='-'):
    t*=-1
print(abs(complex(k,t)))
print(cmath.phase(complex(k,t)))

"""
cmath.phase

This tool returns the phase of complex number z (also known as the argument of z).

>>> phase(complex(-1.0, 0.0))
3.1415926535897931


abs

This tool returns the modulus (absolute value) of complex number z.

>>> abs(complex(-1.0, 0.0))
1.0

"""
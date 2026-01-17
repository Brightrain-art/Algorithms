import math

A, B = map(int, input().split())

fa = math.factorial(A)
fb = math.factorial(B)
fc = math.factorial(A-B)

print(int(fa/fb/fc))

"""

def fac_for(n):
    fir = 1
    for i in range(1, n+1):
        fir *= i
    return fir

A, B = map(int, input().split())

a = fac_for(A)
b = fac_for(B)
c = fac_for(A-B)

print(int(a/b/c))

"""

A, B = map(int, input().split())

kf, nkf, nf = 1, 1, 1

for d in range(1, B+1):
    kf = kf*d
for d in range(1, A-B+1):
    nkf = nkf *d
for d in range(1, A+1):
    nf = nf*d

print(int(nf/kf/nkf))

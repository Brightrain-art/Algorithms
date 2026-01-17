A, B = map(int, input().split())
fir = []
sco = []

for d in range(2, A):
    if A % d == 0:
        fir.append(d)
for i in range(2, B):
    if B % i == 0:
        sco.append(i)

maxi = []

for a in fir:
    if a in sco:
        maxi.append(a)

print(max(maxi))

mul = []
for b in range(1, B+1):
    aa = A*b
    for c in range(1, A*1):
        bb = B*c
        if aa == bb:
            mul.append(aa)

print(min(mul))

"""
0116 / 2609 - timeover
"""

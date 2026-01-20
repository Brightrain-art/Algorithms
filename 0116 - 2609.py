A, B = map(int, input().split())

a, b = A, B

while b:
    a, b = b, a%b

c = a

d = A * B // c

print(c)
print(d)

"""
origin:

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


이 문제도 해결은 했으나 시간초과로 오답인 문제
수학적인 개념이 모자라 못 푼 문제이다. '유클리드 호제법' 이라는 계산법을 이용해 쉽고 간단하게 해결할 수 있었고
최대공배수 또한 쉽게 구해냈다.
"""


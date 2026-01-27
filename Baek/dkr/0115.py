N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
while max(lst) > M :
    lst.pop(max(lst))
    N = N - 1

num_sum = []

for d in lst:
    for a in lst:
        if d != a:
            for b in lst:
                if a != b != d:
                    num_sum.append(a+b+d)

num_sum.sort()
s = num_sum[-1]

while s > M :
    del num_sum[-1]
    s = num_sum[-1]

print(s)

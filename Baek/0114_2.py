N = int(input())
lst = list(map(int, input().split()))

prime = 0
for d in lst:
    num = 0
    if d == 1:
        continue
    for k in range(2,d):
        if d%k == 0:
            num += 1
    if num == 0:
        prime += 1
print(prime)
        

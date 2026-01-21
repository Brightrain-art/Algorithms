n = int(input())
p = list(map(int, input().split()))

p.sort()
total = 0
summary = 0

for i in p:
    total += i
    summary += total

print(summary)
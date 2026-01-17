A, B = map(int, input().split())

a, b = A, B

while b:
    a, b = b, a%b

g = a

l = A * B / g

print(g)
print(l)

"""
0117 - revise 0116
"""

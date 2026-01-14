N = int(input())
lst = [S, M, L, XL, XXL, XXXL] = list(map(int, input().split()))
T, P = map(int, input().split())

total = 0

for i in lst:
    if i%T:
        total = total+i//T+1
    else:
        total = total+i//T

print(total)
print(N//P, N%P)

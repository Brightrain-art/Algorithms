# DP

import sys
input = sys.stdin.readline

T = int(input())
n = [int(input()) for _ in range(T)]

max_n = max(n)

dp = [0] * (max_n + 1)

if max_n >= 1:
    dp[1] = 1
if max_n >= 2:
    dp[2] = 2
if max_n >= 3:
    dp[3] = 4

for i in range(4, max_n+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for d in range(T):
    print(dp[n.pop(0)])


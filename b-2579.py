# DP 개념

import sys
input = sys.stdin.readline

stair = int(input().strip())
scores = [0] + [int(input()) for _ in range(stair)]

dp = [0] * (stair + 1)

if stair >= 1:
    dp[1] = scores[1]
if stair >= 2:
    dp[2] = dp[1] + scores[2]
if stair >= 3:
    dp[3] = max(dp[1] + scores[3], scores[2] + scores[3])

for n in range(4, stair+1):
    dp[n] = max(dp[n-2] + scores[n], dp[n-3] + scores[n-1] + scores[n])

print(dp[stair])
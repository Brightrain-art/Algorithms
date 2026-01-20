# DP 에 대해서 공부했다.
# 로직은 문제없이 이해했는데 코드가 왜 저렇게 되는지 이해하는데 시간이 걸림
# 해결은 했지만 아직 더 공부가 필요함

import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [0] * (n + 1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])


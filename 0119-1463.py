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

# DP 에 대해서 공부했다.
# 로직은 문제없이 이해했는데 코드가 왜 저렇게 되는지 이해하느라 고생좀 했다.
# 아직 조금 모호한 것 같아서 관련 문제를 좀 풀어야겠다고 느낌

# count_0, count_1 = [[], []]
# def fibonacci(n: int):
#     global count_0, count_1
#     if n == 0:
#         count_0.append(0)
        
#         return 0
#     elif n == 1:
#         count_1.append(1)
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# fibonacci(int(input()))
# print(count_0.count(0), count_1.count(1))

tc = int(input())
count_0, count_1 = [[], []]
def fibonacci(n: int):
    dp = [0] * (n + 1)
    if n == 0:
        count_0.append(0)
        dp[0] = 0
        return 0
    elif n == 1:    
        count_1.append(0)
        dp[1] = 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2), dp[n-1] + dp[n-2]
    
fibonacci(int(input()))
print(count_0.count(0), count_1.count(1))

# dp 값에 리스트를 넣어서 


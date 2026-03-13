# BOJ - 2805


N, M = map(int, input().split())
tree_info = list(map(int, input().split()))

start = 0
end = max(tree_info)
result = 0

while start <= end:
    bias = (start + end) // 2
    total = 0

    for height in tree_info:
        if height > bias:
            total += height - bias

    if total >= M:
        result = bias
        start = bias + 1

    else:
        end = bias


print(bias)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
answer = 0

while left <= right:
    mid = (left + right) // 2

    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
        else:
            break

    if total >= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)




# count = 0
# while True:
#     highest = tree_info[0]
#     snd_height = 0

#     for i in tree_info:
#         if i < highest:
#             snd_height = i
#             break
#         count += 1

#     M -= (highest - snd_height) * count

#     if M <= 0:
#         print(snd_height)
#         break
    
#     for idx in range(N):
#         if tree_info[idx] == highest:
#             tree_info[idx] = snd_height
#         else:
#             break
# BOJ - 18111
# 마인크래프트

import sys
from collections import defaultdict

input = sys.stdin.readline

N, M, B = map(int, input().split())
ground_info = defaultdict(int)
highest = 0
lowest = 257
for _ in range(N):
    for i in map(int, input().split()):
        highest = max(highest, i)
        lowest = min(lowest, i)
        ground_info[i] += 1

# print(ground_info)
best_time = float('inf')
best = -1

for height in range(257):
    dig_block = 0
    pile_block = 0
    time = 0

    for k, v in ground_info.items():
        if k > height:
            dig_block += (k-height) * v
            time += 2 * (k-height) * v
        
        elif k < height:
            pile_block += (height-k) * v
            time += (height-k) * v

    if dig_block + B >= pile_block:
        if time < best_time or (time == best_time and height > best):
            best_time = time
            best = height

print(best_time, best)
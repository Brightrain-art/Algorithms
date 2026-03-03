import sys
input = sys.stdin.readline
print = sys.stdout.write

dots_num = int(input())

dots_list = []
for i in range(dots_num):
    a, b = map(int, input().split())
    dots_list.append([a, b])

dots_list.sort()
dots_list.sort(key= lambda x: x[1])

for i in dots_list:
    [a, b] = i
    print(f'{a} {b}\n')
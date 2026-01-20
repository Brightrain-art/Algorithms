import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
lstn = list(map(str, input().split()))
m = int(input())
lstm = list(map(str, input().split()))

s = set(lstn)

for i in lstm:
    if i in s:
        print(str(1)+'\n')
    else:
        print(str(0)+'\n')

"""

문제는 크게 어렵지 않았지만 시간을 단축시키는데 애 먹은 문제
처음에는 input, print를 그냥 사용했다가 타임오버로 sys를 불러왔다.
sys로도 해결되지 않아서 원래 중복을 in 으로 찾는 코드를 짰는데 그것도 set으로 고친 후 in을 사용했다.
어떤 이유로 시간이 단축되는지 이해가 안돼서 더 공부해봐야할 듯 하다.

"""

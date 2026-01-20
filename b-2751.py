import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for i in range(N)]

nums.sort()

sys.stdout.write("\n".join(map(str, nums)))


"""
origin:

N = int(input())
nums = []

for i in range (N):
    nums.append(int(input()))

nums.sort()
print(*nums, sep='\n')

 출력은 잘 나오는데 시간 초과가 떠서 왜 그런지 찾아봤고 sys 모듈을 활용해 해결함.
 이 문제를 해결하며 input, print 도 무거운 함수라는 걸 알았음.
 sys 모듈을 불러와 stdin.readline / stdout.write 를 사용해 더 빠른 연산이 가능함.
"""

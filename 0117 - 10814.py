import sys
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    num, name = map(str, input().split())
    num = int(num)
    lst.append((num, name))

lst.sort(key=lambda num: num[0])

for i in lst:
    print(i[0], i[1])

"""
N = int(input())
lst = []

for _ in range(N):
    lst.append(input())

lst.sort(key=lambda x: x[1])
print(*lst, sep='\n')
"""
원래 코드가 왜 틀렸는지 잘 모르겠다.
출력은 제대로 나오는데 뭐가 문제였던걸까 나중에 다시 찾아보자
우선 정답이 된 코드를 이해는 했는데 안되는게 왜 그런지 모른다.
의미 없어보이는 sys 모듈은 발버둥의 흔적

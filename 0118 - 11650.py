import sys
input = sys.stdin.readline

N = int(input())
dots = []

for _ in range(N):
    x, y = map(int, input().split())
    dots.append((x, y))

dots.sort(key=lambda x: x[1])
dots.sort(key=lambda x: x[0])

dot = [tuple(map(str, t)) for t in dots]

for i in dot:
    sys.stdout.write(f"{i[0]} {i[1]}\n")

"""
시간이 조금 짧은 것 같아서 시간초과 날까봐 처음부터 sys 모듈을 불러왔는데 그렇지만도 않은가보다. 정답을 맞추고
for i in dot:
    print(*i)
  마지막 출력만 프린트로 바꿔서 제출해봤더니 똑같이 정답. 시간도 얼마 차이 안났다.
입력이나 출력보다는 하나씩 센다거나 하는 과정들이 시간을 많이 잡아먹는 듯?

!!!
놀랍게도 이 문제에서는 lambda가 필요 없다고한다.
1번 원소를 오름차순으로 정리하고 1번 원소가 같으면 2번 원소를 오름차순으로 정리하는데
.sort() 메소드 자체가 그런 기능이 있어서 lambda는 불필요하다는 말.
이전에 풀었던 나이와 이름 정렬은 이름이 오름차순으로 정리되면 안되기 때문에 lambda를 사용해 나이만 오름차순으로 정렬한 것이었다.
!!!

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
for i in arr:
    print(i[0], i[1])

지금 내가 만들 수 있는 최고로 간단한 형태.

"""

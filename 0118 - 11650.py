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
"""

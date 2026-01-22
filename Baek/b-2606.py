# 2026-01-21
# 01 ~ 

# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.


# 02
# 튜플로 이뤄진 시퀀스를 만들고 여러 번 훑어야하는 문제인 것 같음
#  => 



# 01
# 인풋을 집합으로 받고 다음 인풋을 받을 때마다 집합에 원소가 있는지 확인 후 있으면 집합 추가, 없으면 버림. 최종 원소의 개수를 출력.
import sys
input = sys.stdin.readline

num_com = int(input().strip())
num_couple = int(input().strip())

comset = set()

a, b = map(int, input().split())
comset.add(a)
comset.add(b)

for _ in range(num_couple-1):
    c, d = map(int, input().split())
    if c in comset:
        comset.add(c)
        comset.add(d)
    if d in comset:
        comset.add(c)
        comset.add(d)

print(len(comset)-1)
# 첫 인풋에 1번 컴퓨터가 있다는 보장이 없어 위의 코드는 잘못되었다.




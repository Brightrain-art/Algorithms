# BOJ - 18310 - 안테나

'''
평균값?

[1] 완전탐색

[2] 집 위치 시작값부터 끝까지 모든 지점을 한 번씩 기준으로 잡고 거리를 다 계산한다.

[3] 20만 * 10만

[4] 모든 집 위치의 평균
'''


N = int(input())
house_pos = list(map(int, input().split()))
status = set(house_pos)

result = set()
mini = float('inf')
for i in status:
    flag = False
    total_dis = 0
    for j in house_pos:
        total_dis += abs(i - j)
        if total_dis > mini:
            flag = True
            break

    if not flag:
        result.add((i, total_dis))
        mini = total_dis


antena_pos = min(result, key=lambda x: (x[1], x[0]))

print(antena_pos[0])


N = int(input())
house_pos = list(map(int, input().split()))

house_pos.sort()

print(house_pos[(N - 1) // 2])
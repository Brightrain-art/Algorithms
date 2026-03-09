# BOJ - 18111

'''
[1] 가장 높은 부분과 가장 낮은 곳을 찾고 그 차를 구한다.

[2] 그 둘이 같다면 소요 시간 0
 - 차이가 1이라면 둘 중 하나를 

[-] 배열로 풀 필요가 없는데?
[-] 집합에 업데이트 하면서 값을 하나로 만들면 된다.
[-] 집합은 정렬을 못한다.

[1] 블록을 꺼내서 놓는 것 - 1초
    블록을 인벤토리에 넣는 것 - 2초
[2] 놓는 걸로 끝낼 수 있다면 놓기만 하는게 빠르다?

[-] 기준을 세워야하는데
[-] 평균값?

[1] 평균값으로 기준을 설정하고
[2] 채워야하는 블럭의 수를 구한다.
[3] 그 수가 인벤토리의 블럭으로 가능하면 채우고
[4] 부족하면 위에서 깎아내고 채운다.
 [4-1] [-][2] 고려해서 차이가 1이고 인벤토리가 비어있다면 가장 높은 값을 모두 하나씩 깎는다.
[5] 반복?

[-] 고려사항
[1] 이미 따잉 평탄하다면 시간은 0초
[2] 차이가 1이라면 고려할게 많아진다.
 - 우선 예제 3만 봐도 차이가 1인데 낮은 곳을 채울 수가 없으니 높은 걸 전부 깎았다.
'''

import sys
from collections import defaultdict
# import time
input = sys.stdin.readline


# start_time = time.time()

def get_standard(info: dict):
    global N, M

    total = 0
    for k, v in info.items():
        total += k * v

    avg = total / (N * M)
    if avg >= int(avg)+0.5:
        avg = int(avg) + 1
    else:
        avg = int(avg)

    return avg


def need_block(info: dict, standard: int):
    need = 0
    for k, v in info.items():
        if k < standard:
            need += (standard - k) * v
    # for block in info:
    #     if block < standard:
    #         need += 1
    
    return need


def make_even(highest: int, lowest: int, inventory: int):
    global ground_info, N, M

    time = 0
    standard = get_standard(ground_info)

    while (True):
        if highest == lowest:
            return time, highest

        # [1] 평균값으로 기준을 설정하고
        # [2] 채워야하는 블럭의 수를 구한다.
        need = need_block(ground_info, standard)
        flag = False

        # [3] 그 수가 인벤토리의 블럭으로 가능하면 채우고
        # [4] 부족하면 위에서 깎아내고 채운다.
        # [4-1] [-][2] 고려해서 차이가 1이고 인벤토리가 비어있다면 가장 높은 값을 모두 하나씩 깎는다.
        '''
        standard == lowest:
        flag = True

        highest == lowest:
        time = 0
        '''
        if need > inventory:
            flag = True

        if standard == lowest:
            flag = True
        
        if flag:
            ground_info[highest-1] += ground_info[highest]
            inventory += ground_info[highest]
            time += 2 * ground_info[highest]
            ground_info.pop(highest)
            highest -= 1

        else:
            ground_info[lowest+1] += ground_info[lowest]
            inventory -= ground_info[lowest]
            time += 1 * ground_info[lowest]
            ground_info.pop(lowest) 
            lowest += 1 

        # if flag:
        #     for idx in range(N*M):
        #         if ground_info[idx] == highest:
        #             ground_info[idx] -= 1
        #             inventory += 1
        #             time += 2
        #     highest -= 1

        # else:
        #     for idx in range(N*M):
        #         if ground_info[idx] == lowest:
        #             ground_info[idx] += 1
        #             inventory -= 1
        #             time += 1
        #     lowest += 1


N, M, B = map(int, input().split())
# ground_info = []
ground_info = defaultdict(int)
highest = 0
lowest = 256
# for _ in range(N):
#     for i in map(int, input().split()):
#         highest = max(highest, i)
#         lowest = min(lowest, i)
#         ground_info.extend([i])

for _ in range(N):
    for i in map(int, input().split()):
        highest = max(highest, i)
        lowest = min(lowest, i)
        ground_info[i] += 1


print(*make_even(highest, lowest, B))

# end_time = time.time()
# elapsed_time = end_time - start_time
# print(elapsed_time)
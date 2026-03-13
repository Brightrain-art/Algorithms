# SWEA - 5202 - 화물 도크

'''
최대한 많은 화물차가 하역을 할 수 있도록 하면 최대 몇 대가 이용할 수 있을까

[1] 그리드

[2] 종료시간이 빠른 것 부터

'''

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    trucks = [list(map(int, input().split())) for _ in range(N)]

    trucks.sort(key=lambda x: x[1])
    # print(trucks)

    count = 1
    _, last_end = trucks[0]

    for start, end in trucks[1:]:
        if start >= last_end:
            count += 1
            last_end = end
    
    print(f"#{test_case} {count}")
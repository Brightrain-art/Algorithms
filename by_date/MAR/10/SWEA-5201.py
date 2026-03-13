# SWEA - 5201 - 컨테이너 운반

'''
N개의 컨테이너를 M대의 트럭으로 운반

트럭 한 대당 한 개, 용량 초과 x

중량이 최대가 되도록 컨테이너를 옮겼다면 화물의 전체 무게 구하기

화물을 싣지 못한 트럭이 있을 수도 있고 화물이 남을 수도 있다.

[1] 그리드?

[2] 남은 화물 中 옮길 수 있는 것들 中 가장 무거운 화물을 옮긴다.

'''

TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    weight_lst = list(map(int, input().split()))
    truck_lst = list(map(int, input().split()))


    container_pointer = 0
    truck_pointer = 0

    weight_lst.sort(reverse=True)
    truck_lst.sort(reverse=True)

    result = 0

    while container_pointer < N and truck_pointer < M:
        if weight_lst[container_pointer] > truck_lst[truck_pointer]:
            container_pointer += 1
        else:
            result += weight_lst[container_pointer]
            container_pointer += 1
            truck_pointer += 1

    print(f"#{test_case} {result}")
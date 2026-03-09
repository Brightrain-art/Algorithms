# SWEA - 1244 최대 상금

'''
[1] 완전탐색

[2] 최대 자릿수 6, 최대 교환 횟수 10
    - 총 볼륨이 그렇게 크지 않음

[3] 순열 탐색


'''



TC = int(input())
for test_case in range(1, TC+1):
    cards, change_op = input().split()
    N = len(cards)
    change_op = int(change_op)
    card = [i for i in list(cards)]
    changed = [False] * N

    # 앞에서부터 큰걸로 바꿔간다.
    pointer = 0
    while pointer < N - 2 and change_op > 0:

        highest = max(card[pointer:])
        for i in range(N-1, pointer, -1):
            if card[i] == highest:
                highest_idx = i
                break
            
        cur_point_val = card[pointer]

        if card[pointer] != highest:
            card[pointer], card[highest_idx] = highest, cur_point_val
            changed[pointer] = changed[highest_idx] = True
            change_op -= 1
            pointer += 1
        else:
            pointer += 1

    if change_op % 2 != 0:
        card[-1], card[-2] = card[-2], card[-1]

    print(f"#{test_case}", "".join(card))
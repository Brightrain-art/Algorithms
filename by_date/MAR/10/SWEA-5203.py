# SWEA - 5203 - 베이비진 게임

'''
베이비진

마지막 카드부터 앞으로 세개까지만 확인하면 됨.

[1] 시뮬레이션?

[2] 카드 분배를 할 때, 길이가 3 이상이 되면 확인을 시작하고
    이전 두 장이 연속이면 run 판별을, 동일하면 triplet 을 확인하자.

'''

def baby_gin(player: list):
    player.sort()

    triple_run = 1
    run_run1 = 1
    for idx in range(1, len(player)):
        # if player.count(player[idx]) == 3:
        if player[idx-1] == player[idx]:
            triple_run +=1
            if triple_run == 3:
                return True
        else:
            triple_run = 1

    player = set(player)
    player = list(player)
    for idx in range(1, len(player)):
        if player[idx-1] + 1 == player[idx]:
            run_run1 += 1
            if run_run1 == 3:
                return True
        else:
            run_run1 = 1

    return False


TC = int(input())
for test_case in range(1, TC+1):
    cards = list(map(int, input().split()))

    p1 = []
    p2 = []
    p1_flag = False
    p2_flag = False

    for i in range(12):
        cur_card = cards[i]
        if i % 2 == 0:
            p1.append(cur_card)
            if i > 3:
                if baby_gin(p1):
                    p1_flag = True
                    break
        else:
            p2.append(cur_card)
            if i > 4:
                if baby_gin(p2):
                    p2_flag = True
                    break

    if p1_flag:
        print(f'#{test_case} 1')
    elif p2_flag:
        print(f'#{test_case} 2')
    else:
        print(f"#{test_case} 0")



    # print(p1, p2)
# SWEA - 1244 최대 상금

def dfs(cnt):
    global cards, change_op, checked, N, best

    result = "".join(cards)

    if (cnt, result) in checked:
        return

    checked.add((cnt, result))

    if cnt == change_op:
        best = max(best, int(result))
        return
    
    for i in range(N-1):
        for j in range(i+1, N):
            cards[i], cards[j] = cards[j], cards[i]
            dfs(cnt + 1)
            cards[i], cards[j] = cards[j], cards[i]

    pass


TC = int(input())
for test_case in range(1, TC+1):
    cards, change_op = input().split()
    cards = [i for i in list(cards)]
    change_op = int(change_op)
    checked = set()
    N = len(cards)

    best = 0
    dfs(0)

    print(f"#{test_case} {best}")
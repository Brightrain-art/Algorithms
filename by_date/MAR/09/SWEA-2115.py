# SWEA - 2115 - 벌꿀채취

'''
허니허니 벌꿀벌꿀

[1] DFS, DP?

[2] 선택이 한 칸이 아니다.
    구역 나누는 데 신경쓰자

[3] 최대 채취량이 있다.
    근데 한 벌통에서 일부만 할 수는 없다. 냅색?

[4] 꿀통에 들어있는 꿀의 양 제곱만큼 수익을 얻을 수 있다.

[-]
'''

import sys
sys.stdin = open('input.txt')

def dfs(r: int, c: int, cur: int, val: int, idx: int):
    global N, M, C, best

    # 제한인 C를 넘어가면 실패
    if cur > C:
        # print(f"{idx}번째 cur {cur}")
        return 
    
    # M개 확인하면 종료
    if idx == M:
        # print(f'{idx}번째 val {val}')
        best = max(best, val)
        return

    
    # 선택할지 안할지
    # print(f'{idx} 선택 안함')
    dfs(r, c+1, cur, val, idx+1)
    # print(f'{idx} 선택 함')
    dfs(r, c+1, cur + field[r][c], val + field[r][c]**2, idx+1)



    pass


TC = int(input())
for test_case in range(1, TC+1):
    N, M, C = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    # M개 만큼 오른쪽으로 가니까
    for row1 in range(N):
        for col1 in range(N-M+1):
            for row2 in range(row1, N):
                start = 0
                if row1 == row2:  # 같은 행에서 작업할 때도 신경써야겠지
                    start = col1 + M
                for col2 in range(start, N-M+1):
                    cur_best = 0
                    best =0 
                    # print('1번 시작')
                    dfs(row1, col1, 0, 0, 0)
                    # print('1번 끝')
                    
                    cur_best += best
                    best = 0

                    # print('2번 시작')
                    dfs(row2, col2, 0, 0, 0)
                    # print('2번 끝')

                    cur_best += best

                    result = max(cur_best, result)

    print(f"#{test_case} {result}")
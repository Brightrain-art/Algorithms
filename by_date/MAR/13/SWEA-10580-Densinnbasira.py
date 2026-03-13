# SWEA - 10580 - Densinnbasira

def check_cross(lines: list):

    lines.sort(key=lambda x: (x[0], x[1]))
    cross_count = 0

    for idx, (_, j) in enumerate(lines):
        for k in range(idx):
            if j < lines[k][1]:
                cross_count += 1

    return cross_count


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(N)]

    # 정렬 먼저 하고, 순서대로 보면서 교차되는지 확인
    # if lines[i][0] < lines[i+1][0]:
    #   if line[i][1] > lines[i][1]:
    # 두 인덱스의 부호가 달라지면 카운팅

    print(f"#{test_case} {check_cross(lines)}")
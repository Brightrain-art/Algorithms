TC = int(input())

# for test_case in range(1, 1 + TC):
#     N = int(input()) 
#     arr = [list(map(int, input().split())) for _ in range(N)] # N 번의 입력을 2차원 리스트로 받아냄

for test_case in range(1, TC+1):
    H, W = map(int, input().split()) # H * W 의 격자
    field = [list(map(str, input())) for _ in range(H)]

    # field.append(input() for _ in range(H)) # 필드 행렬

    # 방향 설정
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)] # U, D, L, R 순

    for line in range(H): # 전차 위치 찾기 // 필드 해당 좌표 표시
        for tank in range(W):
            if field[line][tank] == '^':
                current_tank_pos = field[line][tank] # 해당 좌표 필드 컨디션
                position = (line, tank) # 전차 위치
                # position = (tank, line) # (y, x)에서 (x, y) 로 변환
                
            if field[line][tank] == 'v':
                current_tank_pos = field[line][tank]
                position = (line, tank)
                # position = (tank, line)

            if field[line][tank] == '<':
                current_tank_pos = field[line][tank]
                position = (line, tank)
                # position = (tank, line)
                
            if field[line][tank] == '>':
                current_tank_pos = field[line][tank] 
                position = (line, tank)
                # position = (tank, line)

            # line = 2 , tank = 1
            # field_condition = field[2][1]
            # position = (1, 2)
                
    N = int(input())
    action = input()
    px, py = position
    for act in action: # action 에서 하나씩 동작 수행
        # 동작마다 분기처리 ? U, D, L, R, S 5개
        # for act in action_string:
            (px, py) = position # line = px, tank = py

            if act == 'U':
                # 방향 설정 할 때 부호에 주의하자. 행렬상에서 위로 올라가는거기 때문에 앞에 죄표가 -가 되야 위로 올라감
                dx, dy = dir[3] # dx = 0, dy = 1
                if 0 <= px+dx < H and 0 <= py+dy < W:
                    after = field[px+dx][py+dy]
                    if after == '.': # 이동 예정 위치 필드 상황 확인
                        position = (px+dx, py+dy) # 평지면 포지션 이동
                        field[px][py], field[px+dx][py+dy] = after, '^' # 둘이 교환
                        # ax, ay = px+dx, py+dy
                        current_tank_pos = field[px+dx][py+dy]

                    else: # 평지가 아니면 이동 안함
                        current_tank_pos = '^' # 방향만 변경
                        field[px][py] = '^'
                        continue
                else:
                    continue

            if act == 'D':
                dx, dy = dir[2]
                if 0 <= px+dx < H and 0 <= py+dy < W:
                    after = field[px+dx][py+dy]
                    if after == '.': # 이동 예정 위치 필드 상황 확인
                        position = (px+dx, py+dy) # 평지면 포지션 이동
                        field[px][py], field[px+dx][py+dy] = after, 'v' # 둘이 교환
                        current_tank_pos = field[px+dx][py+dy]

                    else: # 평지가 아니면 이동 안함
                        current_tank_pos = 'v' # 방향만 변경
                        field[px][py] = 'v'
                        continue
                else:
                    continue

            if act == 'R':
                dx, dy = dir[0]
                if 0 <= px+dx < H and 0 <= py+dy < W:
                    after = field[px+dx][py+dy]
                    if after == '.': # 이동 예정 위치 필드 상황 확인
                        position = (px+dx, py+dy) # 평지면 포지션 이동
                        field[px][py], field[px+dx][py+dy] = after, '>'
                        # current_tank_pos, after = after, '>' # 둘이 교환
                        # ax, ay = px+dx, py+dy
                        current_tank_pos = field[px+dx][py+dy]
                        # field[ax][ay] = after
                        # print(field)

                    else: # 평지가 아니면 이동 안함
                        current_tank_pos = '>' # 방향만 변경
                        field[px][py] = '>'
                        continue
                else:
                    continue

            if act == 'L':
                dx, dy = dir[1]
                if 0 <= px+dx < H and 0 <= py+dy < W:
                    after = field[px+dx][py+dy]
                    if after == '.': # 이동 예정 위치 필드 상황 확인
                        position = (px+dx, py+dy) # 평지면 포지션 이동
                        field[px][py], field[px+dx][py+dy] = after, '<' # 둘이 교환
                        # ax, ay = px+dx, py+dy
                        current_tank_pos = field[px+dx][py+dy]

                    else: # 평지가 아니면 이동 안함
                        current_tank_pos = '<' # 방향만 변경
                        field[px][py] = '<'
                        continue
                else:
                    continue

            # 이동 완료 // 검증 미완

            # 끝까지 쭉 이동한다.
            if act == 'S':
                # 현재 포지션 방향 따라 분기처리 '^', 'v', '>', '<'
                # 현재 포지션 befor == field[px][py]
                # x 축 포탄 이동거리는 W - py(오른쪽) or py(왼쪽)
                # y 축 포탄 이동거리는 H - px(아래) or px(위)
                # px 는 line, H이고 py는 tank, W 임에 주의
                current_tank_pos
                if current_tank_pos == '^':
                    for distance in range(1, px+1):
                        # 위쪽으로 필드 상태 확인
                        if field[px-distance][py] == '*': # 벽돌이면 파괴
                            field[px-distance][py] = '.'
                            break
                        elif field[px-distance][py] == '#': # 강철이면 continue
                            break
                        # 물이나 평지는 무시
                if current_tank_pos == 'v':
                    for distance in range(1, H-px): # H 4 , px 2 
                        # 아래쪽으로 필드 상태 확인
                        if field[px+distance][py] == '*': # 벽돌이면 파괴
                            field[px+distance][py] = '.'
                            break
                        elif field[px+distance][py] == '#': # 강철이면 continue
                            break

                if current_tank_pos == '>':
                    for distance in range(1, W-py):
                        # 위쪽으로 필드 상태 확인
                        if field[px][py+distance] == '*': # 벽돌이면 파괴
                            field[px][py+distance] = '.'
                            break
                        elif field[px][py+distance] == '#': # 강철이면 continue
                            break

                if current_tank_pos == '<':
                    for distance in range(1, py+1):
                        # 위쪽으로 필드 상태 확인
                        if field[px][py-distance] == '*': # 벽돌이면 파괴
                            field[px][py-distance] = '.'
                            break
                        elif field[px][py-distance] == '#': # 강철이면 continue
                            break                

    
    print(f'#{test_case} ',end='')
    for answer in field:
        print(''.join(answer))
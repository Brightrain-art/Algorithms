tc = int(input().strip()) # 테스트 케이스 인풋
n = len(colour_list)

colour_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple'] # 색상환 리스트화
for i in range(tc): # 테스트 케이스만큼 순회
    fst, snd = input().split() # 입력
    f = colour_list.index(fst)
    s = colour_list.index(snd)
    
    if f == s:
        print('E')
    elif (f + 1) % n == s or (f - 1) % n == s:
        print('A')
    elif (f + 3) % n == s:
        print('C')
    else:
        print('x')
    # if colour_list.index(fst) == colour_list.index(snd): # 같으면
    #     print('E')
    #     # 인접하면
    # elif colour_list[colour_list.index(fst) + 1] % 6 == snd or colour_list[colour_list.index(fst) - 1] % 6 == snd:
    #     print('A')
    #     # 마주보면
    # elif colour_list[colour_list.index(fst) + 3] % 6 == snd or colour_list[colour_list.index(fst) - 3] % 6 == snd:
    #     print('C')
    #     # 이외
    # else:
    #     print('X')
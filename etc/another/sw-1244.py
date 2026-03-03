# 리스트를 받는다 (숫자로 주어짐 123, 2737 등)
# 리스트 인덱스 교환 가능 횟수가 주어진다
# 지정 횟수만큼 교환해서 가능한 만큼 내림차순 정리 수행

# 카드 개수는 최대 6개, 최대 교환 횟수는 10번
# cards, time = input().split() # str, str


# cards_list = []
# for i in cards:
#     cards_list.append(int(i)) # 입력 순으로 리스트 추가 : int

# 제일 큰게 왼쪽, 작은게 오른쪽 / 반드시 교환을 하긴 해야 함
# 최댓값은 인덱스 0에 두고 최솟값은 마지막 인덱스로

# 1. 최댓값 인덱스 0
# 2. 최솟값 인덱스 마지막
# 3. 두번째 최댓값 인덱스 1
# 4. 두번째 최솟값 인덱스 마지막-1
# 투포인터 개념이랑 비슷한데?

# cards_list = [3, 2, 8, 8, 8]
# left = 0
# print(cards_list.index(max(cards_list)))
# cards_list[left], cards_list[cards_list.index(max(cards_list))] = cards_list[cards_list.index(max(cards_list))], cards_list[left]
# cards_list[0], cards_list[2] = cards_list[2], cards_list[0]

# cards_list[left] = 8
# cards_list[cards_list.index(max(cards_list))] = 3
# print(cards_list)

tc = int(input())
test_case = 0
for i in range(tc):

    cards, time = input().split() # str, str

    cards_list = []
    for i in cards:
        cards_list.append(int(i)) # 입력 순으로 리스트 추가 : int

    def cards_arr():
        pass
        left, right = 0, len(cards_list) - 1
        c = cards_list
        t = int(time)
        goal_list = cards_list.copy()
        goal_list.sort(reverse= True)

        # 변환 가능 횟수 제한
        while t > 0:
            goal_left = cards_list.index(goal_list[left])
            goal_right = cards_list.index(goal_list[right])
            # mi = cards_list.index(min(cards_list))
            # 최댓값 인덱스 0
            if cards_list[left] < cards_list[goal_left]:
                cards_list[left], c[goal_left] = c[goal_left], cards_list[left]
                t -= 1
                left += 1
                if left == right:
                    break
                if t == 0:
                    continue
                # continue

            # 최솟값 인덱스 마지막
            if c[right] > c[goal_right]:
                c[right], c[goal_right] = c[goal_right], c[right]
                t -= 1
                right -= 1
            
                if t == 0:
                    continue
                # continue

            # 최댓값과 최솟값이 각자 자리에 갔을 때
            if c[left] == c[goal_left]:
                left += 1
                if left == right:
                    break
                continue

            if c[right] == c[goal_right]:
                right -= 1
                continue

            if cards_list == goal_list:
                break
        
        while t > 0:
            cards_list[len(cards_list)- 1], cards_list[len(cards_list)- 2] = cards_list[len(cards_list)- 2], cards_list[len(cards_list)- 1]
            t -= 1

        return ''.join(map(str, cards_list))

    test_case += 1

    print(f'#{test_case} {cards_arr()}')


# def reverse_string(s: list[str]):
#     left, right = 0, len(s) - 1
#     # 왼쪽은 인덱스 0부터 오른쪽은 마지막 인덱스(s - 1) 부터
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
#     return s
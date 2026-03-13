# SWEA - 20551 - IncreasingCandy

def check_candy(candy_nums: list):

    N = len(candy_nums)
    result = 0
    for i in range(N-1, 0, -1):
        if candy_nums[i-1] >= candy_nums[i]:
            gorge_num = candy_nums[i-1] - candy_nums[i] + 1

            if candy_nums[i-1] - gorge_num <= 0:
                return -1

            candy_nums[i-1] -= gorge_num
            result += gorge_num
    
    return result
            

TC = int(input())
for test_case in range(1, TC+1):

    # 쪼개자
    # 뒤에서부터 보면서
    # 앞에가 사탕이 더 많으면 먹어야한다. 얼마나?
    # 앞에서 뒤에거 뺀거에 + 1 만큼 먹어야한다.
    # lst[i+1] - lst[i] + 1
    # if lst[i] - (lst[i+1] - lst[i] + 1) <= 0: fail
    # lst[i] -= eat

    candy_nums = list(map(int, input().split()))

    print(f"#{test_case} {check_candy(candy_nums)}")
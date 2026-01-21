# 첫 줄에 정수의 개수가 주어지고 다음 줄에 랜덤한 정수가 주어질 때
# 그 정수들 중 최대값 최소값 출력 (공백 구분)

# split 을 이용해 리스트로 구분해 받고 그 안에서 max, min을 이용해 출력

N = int(input())
num_list = list(map(int, input().split()))

print(min(num_list), max(num_list))

# int 를 사용하지 않고 받아 문자열이 되어 max, min이 작동을 안했었음
#  => map과 int 이용해서 해결
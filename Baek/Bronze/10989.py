import sys
input = sys.stdin.readline

N = int(input().strip()) # 인풋 개수

# num_list = [] # 숫자 넣을 리스트
# for i in range(N): # 인풋 개수만큼 반복
#     num_list.append(int(input().strip())) # 숫자 리스트에 추가
# num_list.sort() # 오름차순 정리
# for i in num_list: # 리스트 인덱스 순 반복
#     print(i) # 인덱스순(오름차순) 출력

lst = [0] * 10001
for _ in range(N):
    lst[int(input())] += 1
for i in range(1,10001):
    if lst[i]:
        print(i*lst[i])
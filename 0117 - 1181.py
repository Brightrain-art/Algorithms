n = int(input())
lst = [input() for i in range(n)]

lst = list(set(lst))
lst.sort()
lst.sort(key=len)

for i in lst:
    print(i)


"""
origin:

N = int(input())
lst = []

for _ in range(N):
    w = input()
    if w not in lst:
        lst.append(w)

N = len(lst)
lst.sort()

for d in range(0, N-1):
    while len(lst[d]) > len(lst[d+1]):
        for i in range(0, N-1):
                    lst[i], lst[i+1] = lst[i+1], lst[i]
            

for i in range(0, N-1, 2):
    while len(lst[i]) == len(lst[i+1]):
        lst[i:i+1] = sorted(lst[i:i+1])    
    

for i in lst:
    print(i)

중복 문자 제거는 if문을 활용해 입력과정에서 해결했는데
글자 수 순서 정렬, 알파벳 오름차순 정렬을 각각은 가능하지만 두 가지를 한 번에 해결하지 못했음
이 문제를 해결하며 set / sort(key = len) 등의 기능이 있다는걸 알았음
아마 sys 모듈을 이용해도 좋았을 듯

"""

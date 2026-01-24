num_case = int(input())

for i in range(1, num_case + 1):
    N = float(input())
    Binary = []

    for e in range(1,14): # 13번째 자리까지만 체크
        if N == 0: # N 이 0 되면 for문 종료
            break
        if 2**-e <= N: # N이 1/2의 n승 보다 크거나 같으면 1/2의 n승을 뺀다.
            N -= 2**-e
            Binary.append('1') # Binary에 '1' 추가
        else:
            Binary.append('0') # 작으면 '0' 추가

    if N != 0:
        result = 'overflow' # 13번째 자리까지 다 헀는데 N이 남아있으면 overflow
    else:
        result = ''.join(Binary) # join 메서드를 이용해 출력
        # 숫자열로 추가해도 똑같나? // 안된다.
        # 우선 join은 문자열 전용이고 문제가 계산이 필요한 문제였다면 숫자열이 좋지만 출력만 보는 문제이기에 문자열이 더 편하다.
        # 숫자열로 추가하면 어차피 변환해줘야함
    
    print(f'#{i} {result}')

## 더 깔끔하게 리팩토링 할 수 있을 거 같기도 하고 로직 자체를 바꿔도 좋을 거 같음
## 승우님이 얘기한 나눗셈은 더 깔끔할 거 같은데?


# -----------------------------------------
# CASE 개수 주어지지 않을 때
# 'try' 를 활용해 인풋이 끊길때까지 반복하는 코드
# except EOFError

case_num = 1 # 더미

while True:
    try:
        N = float(input())
        binary = []

        for e in range(1, 14):
            if N == 0:
                break
            if N >= 2**-e:
                N -= 2**-e
                binary.append('1')
            else:
                binary.append('0')

        if N != 0:
            result = 'overflow'
        else:
            result = ''.join(binary)

        print(f'#{case_num} {result}')
        case_num += 1

    except EOFError:
        break


# -------------------------------------------
# 한 개씩 주어질 때는 기능하지만 테스트 케이스가 여러개 되면 돌아가긴 한다만 첫 번째 인풋값의 결과만 반복 출력


num_case = int(input())

N = float(input())
Binary = []
for e in range(1,14):
    if N == 0:
        break
    if 2**-e <= N:
        N -= 2**-e
        Binary.append('1')
    else:
        Binary.append('0')

## 이 부분이 문제였다. 작성할때는 새로운 방법을 찾았다며 신나서 했지만 결국 안되는 코드였다..
## 얘한테 개별 for문이 하나 들어가서 전체를 반복하지 못함
## 이 부분을 살리려고 머리를 계속 박았지만 결국 폐기
## 함수를 짜면 되려나? 나중에 한 번 해봐야지
for i in range(1, num_case + 1): 
    if N != 0:
        print('overflow')
        break
    number = f'#{i} '
    for d in range(len(Binary)):
        number += Binary[d]
    print(number)


# while True:
#     try:
#         N = float(input())
#         Binary = []
#         for e in range(1,14): # 13번째 자리까지만 체크
#             if N == 0: # N 이 0 되면 for문 종료
#                 break
#             if 2**-e <= N: # N이 1/2의 n승 보다 크거나 같으면 1/2의 n승을 뺀다.
#                 N -= 2**-e
#                 Binary.append('1')
#             else:
#                 Binary.append('0')
#         if N != 0:
#             print('overflow')
#             continue
#         i = 1
#         number = f'#{i} '
#         for d in range(len(Binary)):
#             number += Binary[d]
#             print(number)   
#             i += 1
#     except EOFError:
#         break



# for i in range(len(Binary)):
#     num.append(Binary[i])
#     number += Binary[i]
# print(number)

# for i in range(1, num_case + 1):
  

# for i in Binary:
#     print(i, end='')
# print(Binary, sep=' ')

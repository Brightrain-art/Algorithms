# math 모듈을 처음 사용해봤음.
# 문제를 해결하긴 했지만 함수와 모듈을 이용해서 해결하자는 생각은 하지 못헀고 그래서 연산도 오래 걸리고 코드 자체도 길어짐.
# 같은 작업을 반복할 때에는 함수를 사용하고 그 함수가 math 모듈에 존재한다면 적극적으로 활용하자

import math

A, B = map(int, input().split())

fa = math.factorial(A)
fb = math.factorial(B)
fc = math.factorial(A-B)

print(int(fa/fb/fc))


# def fac_for(n):
#     fir = 1
#     for i in range(1, n+1):
#         fir *= i
#     return fir

# A, B = map(int, input().split())

# a = fac_for(A)
# b = fac_for(B)
# c = fac_for(A-B)

# print(int(a/b/c))

# ---

# A, B = map(int, input().split())

# kf, nkf, nf = 1, 1, 1

# for d in range(1, B+1):
#     kf = kf*d
# for d in range(1, A-B+1):
#     nkf = nkf *d
# for d in range(1, A+1):
#     nf = nf*d

# print(int(nf/kf/nkf))



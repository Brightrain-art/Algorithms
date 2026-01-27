# 아주 애먹었던 문제.
# 알고리즘이 어렵진 않았지만 math 모듈을 적용하지 않으니 시간초과로 인해 계속 틀렸다.
# 모듈 사용법을 모른채로 그냥 수식으로만 연산시간을 줄이려니 도저히 안되겠어서 모듈을 익히고 적용해서 해결했다.

import math

A, B, V = map(int, input().split())

if V == A:
    print(1)
elif V > A:
    print(math.ceil((V-A)/(A-B)+1))

# A, B, V = map(int, input().split())

# h = 0
# day = 0
# while h < V:
#     h += A
#     day += 1
#     if h < V:
#         h -= B
# print(day)


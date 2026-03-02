tc = int(input())

for i in range(tc):
    ox = input()
    lst = []
    n = 0
    for j in ox:
        if j == 'O':
            n += 1
            lst.append(n)
        else:
            n = 0
    print(sum(lst))
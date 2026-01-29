tc = int(input().strip())

for t in range(tc):
    R, S = input().split()
    R = int(R)

    for i in S:
        print(i*R, end='')
    print()
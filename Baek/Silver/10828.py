import sys
input = sys.stdin.readline

stacks = []
def stack(strs: str):
    if 'push' in strs:
        stacks.append(int(strs[5:]))
    elif 'top' in strs:
        if stacks:
            print(stacks[-1])
        else:
            print(-1)
    elif 'size' in strs:
        print(len(stacks))
    elif 'empty' in strs:
        if stacks:
            print(0)
        else:
            print(1)
    elif 'pop' in strs:
        if stacks:
            print(stacks.pop(-1))
        else:
            print(-1)

tc = int(input().split())
for _ in range(tc):
    stack(input().split())

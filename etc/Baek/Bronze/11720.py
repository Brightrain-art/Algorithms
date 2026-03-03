N = input()
num = input()
lst = []
for i in range(len(num)):
    lst.append(num[i])
print(sum(map(int, lst)))
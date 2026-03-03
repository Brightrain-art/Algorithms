A = input()
B = input()
C = input()

print(int(A) + int(B) - int(C))

print(int(f'{A}{B}')-int(C), sep=' ')

#-------------------------#

print(int(str(A)+str(B)) - int(C))
T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    splited_S = S.split()
    joined_S = "".join(S)
    for j in joined_S:
        print(j*R, end='')
    print()
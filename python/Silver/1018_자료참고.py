# 자료 참고
N, M = map(int, input().split())
l = []
mini = []

for _ in range(N): # 체스판
    l.append(input())

for a in range(N - 7):
    for i in range(M - 7):
        idx1 = 0
        idx2 = 0
        for b in range(a, a+8):
            for j in range(i, i+8):
                if (j + b)%2 == 0:
                    if l[b][j] != 'W': idx1 += 1
                    if l[b][j] != 'B': idx2 += 1
                else :
                    if l[b][j] != 'B': idx1 += 1
                    if l[b][j] != 'W': idx2 += 1
        mini.append(idx1)
        mini.append(idx2)

print(min(mini))
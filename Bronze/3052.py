N = []
D = []
for i in range(10):
    N.append(input())
for j in N:
    D.append(int(j)%42)

print(len(set(D)))
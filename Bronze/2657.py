T = int(input())
for i in range(1, T+1):
    R, S = input().split()
    S = list(map(str, S))
    N = []
    for j in range(0, len(S)):
        N.append(str(S[j])*R)
        print("".join(N))
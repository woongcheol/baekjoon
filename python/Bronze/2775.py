T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    f0 = [x for x in range(1, n+1)]
    for j in range(1, k+1):
        for k in range(1, n):
            f0[k] = f0[k-1] + f0[k]
    print(f0[n-1])
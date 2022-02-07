def P(n):
    for idx in range(4, n+1):
        data[idx] = data[idx-2] + data[idx-3]
    return data[n]

data = [0]*101
data[0] = 1
data[1] = 1
data[2] = 1
data[3] = 1

T = int(input())
for _ in range(T):
    n = int(input())
    print(P(n))
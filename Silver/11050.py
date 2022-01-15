N, K = map(int, input().split())
sum = 1
for i in range(1, N+1):
    sum *= i # N!

for j in range(1, K+1):
        sum /= j # N!/K!

for k in range(1, N-K+1):
    sum /= k # N! / K!(N-K)!

print(int(sum))
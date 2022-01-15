number, max = map(int, input().split())
sum = list(map(int, input().split()))
sum_max = 0

for i in range(number-2):
    for j in range(1, number-1):
        for k in range(2, number):
            if i != j and i != k and j != k:
                if sum_max <= sum[i] + sum[j] + sum[k] <= max:
                    sum_max = sum[i] + sum[j] + sum[k]
print(sum_max)
N = int(input())

sum = 1
cnt = 1

while N > sum:
    sum += 6 * cnt
    cnt += 1

print(cnt)
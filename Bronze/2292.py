N = int(input())
i = 1
while True:
    i += 1
    if N == 1:
        print(1)
        break
    else:
        for j in range(i+1, i+2):
            if 6 * (i - 1) + 1 < N <= 6 * i + 1:
                print(i)
        break
N = int(input())
kg_3 = 3
kg_5 = 5
cnt = 0

while True:
    devision = N - kg_3 * cnt
    if devision % kg_5 == 0:
        print(int(devision/5)+cnt)
        break
    elif devision < 0:
        print(-1)
        break
    else:
        cnt += 1
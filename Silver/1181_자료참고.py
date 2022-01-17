# 자료 참고
N = int(input())
sort = list()

for _ in range(N):
    sort.append(input())

sort.sort()
sort.sort(key = len)

for i in sort:
    print(i)
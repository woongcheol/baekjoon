# 자료 참고
N = int(input())
sort = list()

for _ in range(N):
    sort.append(input())

print(set(sort))
sort = list(set(sort))
sort.sort()
set = sort.sort(key = len)

for i in sort:
    print(i)
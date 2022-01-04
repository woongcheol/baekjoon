A = int(input())
B = int(input())
C = int(input())

sum = A*B*C
sum = list(map(int, str(sum)))

for i in range(0,10):
    print(sum.count(i))
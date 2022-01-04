N = int(input())
subject = list(map(int, input().split()))
sum = 0
for i in subject:
    sum += i/max(subject)*100
print(sum/N)
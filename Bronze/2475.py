number = list(map(int, input().split()))
unique = 0
for i in number:
    unique += i**2
print(unique%10)
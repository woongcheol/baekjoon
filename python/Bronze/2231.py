number = int(input())
i = 1
min = number
while i < number:
    N = number - i
    T = str(N)
    for j in T:
        N += int(j)
    if N == number:
        min = number - i
    i += 1
if number == min:
    print(0)
else:
    print(min)
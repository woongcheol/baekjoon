number = []
for i in range(0, 9):
    number.append(int(input()))
print(max(number))
print(number.index(max(number))+1)
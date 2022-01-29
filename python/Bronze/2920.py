N = map(int, input().split())
change_N = list(N)

for i in range(8):
    if change_N[i] == 1:
        change_N[i] = 'c'
    elif change_N[i] == 2:
        change_N[i] = 'd'
    elif change_N[i] == 3:
        change_N[i] = 'e'
    elif change_N[i] == 4:
        change_N[i] = 'f'
    elif change_N[i] == 5:
        change_N[i] = 'g'
    elif change_N[i] == 6:
        change_N[i] = 'a'
    elif change_N[i] == 7:
        change_N[i] = 'b'
    elif change_N[i] == 8:
        change_N[i] = 'C'

if "".join(change_N) == 'cdefgabC':
    print('ascending')
elif "".join(change_N) == 'Cbagfedc':
    print('descending')
else:
    print('mixed')
A, B = input().split()
reverse_A = int(''.join(reversed(list(A))))
reverse_B = int(''.join(reversed(list(B))))
if reverse_A > reverse_B:
    print(reverse_A)
else:
    print(reverse_B)
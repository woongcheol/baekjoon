H, M = map(int, input().split())
if M > 45:
    print(f'{H} {M-45}')
elif M == 45:
    print(f'{H} {0}')
else:
    if H != 0:
        print(f'{H-1} {M+15}')
    else:
        print(f'{23} {M+15}')
# stop = 0
# while stop == 0:
#     A, B, C = map(int, input().split())
#     if A == 0 and B == 0 and C == 0:
#         stop += 1
#     elif C**2 == A**2 + B**2:
#         print("right")
#     else:
#         print("wrong")
while True:
    N = list(map(int, input().split()))
    max_num = max(N)
    if sum(N) == 0:
        break
    N.remove(max_num)
    if N[0]**2 + N[1]**2 == max_num**2:
        print("right")
    else:
        print("wrong")
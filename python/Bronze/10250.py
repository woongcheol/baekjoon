# 불합격
# T = int(input())
# for i in range(T):
#     H, W, N = map(int, input().split())
#     R = []
#     for i in range(N): # 손님 수 만큼 배정
#         while len(R) != N:
#             if len(R) == N: # 모두 배정되면 중단
#                 break
#             else:
#                 for i in range(1, W+1): # 호 수 만큼 배정
#                     if len(R) == N: # 모두 배정되면 중단
#                         break
#                     else:  
#                         for j in range(1, H+1): # 층 수 만큼 배정
#                             if len(R) == N: # 모두 배정되면 중단
#                                 break
#                             elif i < 10: # 1 ~ 9호일 경우
#                                 if R.count(f'{j}0{i}') == 0: # 동일 값이 없다면 입력
#                                     R.append(f'{j}0{i}')
#                                 else: # 동일 값이 있다면 다음 층 탐색
#                                     break
#                             else: # 10호 이상일 경우
#                                 if R.count(f'{j}0{i}') == 0: # 동일 값이 없다면 입력
#                                     R.append(f'{j}0{i}')
#                                 else: # 동일 값이 있다면 다음 층 탐색
#                                     break
#     print(int(R[-1]))


T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    R = []
    if len(R) == N: # 고객 수만큼 배정시 종료
        break
    else:
        for i in range(1, W+1):
            if len(R) == N: # 고객 수만큼 배정시 종료
                break
            else:
                for j in range(1, H+1):
                    if len(R) == N: # 고객 수만큼 배정시 종료
                        break
                    else:
                        if i < 10: # 9호 이하일 경우
                            R.append(f'{j}0{i}')
                        else: # 10호 이상일 경우
                            R.append(f'{j}{i}')
    print(R[-1])
# 시간 초과
# A, B, V = map(int, input().split())
# day = 1 # day 만큼 반복문 실행해서 시간 초과
# while V != 0:
#     V -= A
#     if V <= 0:
#         print(day)
#         break
#     else:
#         V += B
#         day += 1

A, B, V = map(int, input().split())
day = (V-B)/(A-B) # A*day-B(day-1) >= V -> day >= (V-B)/(A-B)
print(int(day) if day == int(day) else int(day)+1) # 삼항 연산자
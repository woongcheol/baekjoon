# 런타임 에러
while True:
    string = input()
    left = 0
    right = 1
    if string == '0':
        break

    if len(string) % 2 == 0:
        for _ in range(int(len(string)/2)):
            if string[left] == string[-right]:
                if left == int(len(string)/2)-1:
                    print('yes')
                left += 1
                right += 1
            elif string[left] != string[-right]:
                print('no')
                break
    else:
        for _ in range(int(len(string)/2)):
            if string[left] == string[-right]:
                if left == int(len(string)/2-1):
                    print('yes')
                left += 1
                right += 1
            elif string[left] != string[-right]:
                print('no')
                break

# while True:
#     n = input()

#     if n == '0':
#         break
    
#     if n == n[::-1]:
#         print('yes')
#     else:
#         print('no')
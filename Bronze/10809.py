"""
for 문, map 객체 정리

A = input() # 문자열 입력, 문자열 반환
print(type(A)) # str
print(A)
for i in A: # 시퀀스 객체(문자열)
    print(i) # a, b, c, d

B = input().split() # 문자열 입력, 문자열 리스트 반환
print(type(B)) # list
print(B)
for i in B: # 시퀀스 객체(문자열 리스트)
    print(i) # abcd

C = map(str, input().split()) # 문자열 입력, 맵 객체 반환
print(type(C)) # map
print(C)
for i in C: # 시퀀스 객체(맵)
    print(i) # abcd
"""

S = input()
T = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(T)):
    j = 0
    while j < len(S):
        if T[i] == S[j]:
            print(S.index(S[j]), end=" ")
            break
        elif j == 3 and T[i] == "z":
            print(-1)
            break
        elif j == 3:
            print(-1, end=" ")
            j += 1
        else:
            j += 1
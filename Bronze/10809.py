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

# S = input()
# T = list(range(97,123))
# for i in range(len(T)):
#     j = 0
#     while j < len(S):
#         if T[i] == "z" and T[i] == S[j]: # 마지막 z가 같을 경우
#             print(S.index(S[j]))
#             break
#         elif T[i] == S[j]: # T 요소와 같을 경우
#             print(S.index(S[j]))
#             break
#         elif T[i] == "z": # 마지막 z가 없을 경우
#             print(-1)
#             break
#         else: # 없을 경우
#             if j == len(S)-1:
#                 print(-1)
#             j += 1

word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x)))
    print(type(word.find(chr(x)))) 
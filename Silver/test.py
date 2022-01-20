from sys import stdin

N = stdin.readline()
number = sorted(map(int, stdin.readline().split()))
M = stdin.readline()
find_number = list(map(int, stdin.readline().split()))

def binary(l, number, start, end):
    
    # 시작이 종료를 넘을 경우 종료
    if start > end:
        return 0

    # 중간 값 찾기
    m = (end+start)//2
    
    # 찾는 값이 m이랑 같을 때
    if l == number[m]:
        return 1

    # 찾는 값이 m보다 작을 때
    elif l < number[m]:
        return binary(l, number, start, m-1)

    # 찾는 값이 m보다 클때
    else:
        return binary(l, number, m+1, end)



for l in find_number:
    start = 0
    end = len(number)-1
    print(binary(l, number, start, end))
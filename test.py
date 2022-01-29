from sys import stdin
from collections import deque

def input_deque(message):
    
    if message[0] == 'pop_front':
        if in_deque:
            print(in_deque.popleft())
        else:
            print(-1)

    elif message[0] == 'pop_back':
        if in_deque:
            print(in_deque.pop())
        else:
            print(-1)

    elif message[0] == 'size':
        print(len(in_deque))

    elif message[0] == 'empty':
        if in_deque:
            print(0)
        else:
            print(-1)

    elif message[0] == 'front':
        if in_deque:
            print(in_deque[0])
        else:
            print(-1)

    elif message[0] == 'back':
        if in_deque:
            print(in_deque[-1])
        else:
            print(-1)

    elif message[0] == 'push_front':
        in_deque.appendleft(message[1])

    elif message[0] == 'push_back':
        in_deque.append(message[1])

N = int(input())
in_deque = deque([])

for i in range(N):
    message = stdin.readline().split()
    input_deque(message)
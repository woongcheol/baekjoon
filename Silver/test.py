from collections import deque

N = int(input())
card = deque([num for num in range(1, N+1)])

def card_remain(card):
    while len(card) > 1:
        card.popleft()
        move_num = card.popleft()
        card.append(move_num)

    return card.pop()

print(card_remain(card))
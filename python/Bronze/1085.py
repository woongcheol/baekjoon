x, y, w, h = map(int, input().split())
if w-x >= x: # x 좌표가 0에 근접할 때
    if h-y >= y: # y 좌표가 0에 근접할 때
        if x > y:
            print(y)
        else:
            print(x)
    else: # y 좌표가 h에 근접할 때
        if x > h-y:
            print(h-y)
        else:
            print(x)
if w-x < x: # x 좌표가 w에 근접할 때
    if h-y >= y: # y 좌표가 0에 근접할 때
        if w-x > y:
            print(y)
        else:
            print(w-x)
    else: # y 좌표가 h에 근접할 때
        if w-x > h-y:
            print(h-y)
        else:
            print(w-x)
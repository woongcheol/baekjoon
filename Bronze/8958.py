T = int(input())
for i in range(T):
    sum = 0
    problem = input()
    for j in range(len(problem)):
        if problem[j] == "O":
            sum += 1
            k = j + 1
            while k < len(problem):
                if problem[k] == "O":
                    sum += 1
                    k += 1
                    continue
                elif problem[k] == "X":
                    break
    print(sum)
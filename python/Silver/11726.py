def squear(n):
    for idx in range(2, n+1):
        memory[idx] = memory[idx-1] + memory[idx-2]
    return memory[n]

n = int(input())
memory = [0 for _ in range(0, n+1)]
memory[0] = 1
memory[1] = 1
print(squear(n))
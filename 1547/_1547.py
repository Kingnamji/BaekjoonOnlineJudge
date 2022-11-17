M = int(input())

position = 1 # initial position

for _ in range(M):
    X, Y = map(int, input().split())

    if position == X:
        position = Y
    elif position == Y:
        position = X

print(position)
    

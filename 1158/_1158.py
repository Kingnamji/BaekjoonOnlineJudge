N, K = map(int, input().split())

ary = [i for i in range(1, N+1)]
result = []

idx = K-1 # initial person

print("<", end="")

while 1:
    eliminated = ary.pop(idx)
    print(eliminated, end="")

    
    if not ary:
        break # eliminate all.....

    print(", ", end ="")
    idx = (idx + K -1) % len(ary)
    

print('>', end="")

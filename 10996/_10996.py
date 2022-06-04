# 10996 별 찍기 - 21
N = int(input())

if (N%2): # N => 홀수
    first = N//2 + 1
    second = N//2
else: # N => 짝수
    first = N//2
    second = N//2 

for _ in range(N):
    print( "* " *  first)
    print( " *" *  second)

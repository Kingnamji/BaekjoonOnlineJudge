# 1049 기타줄
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
minPack = 9999
minOne = 9999

def testNum(n):
    if ((n/6)%1) == 0:
        return True
    else:
        return False

for _ in range(M):
    a, b = map(int, input().split())
    if minPack >= a:
        minPack = a
    if minOne >= b:
        minOne = b

case = []

if testNum(N):
    case.append((N//6)*minPack)
    case.append(N*minOne)
else:
    case.append( ((N//6)+1)*minPack )
    case.append( (N//6)*minPack + (N%6)*minOne )
    case.append( N*minOne )

print(min(case))

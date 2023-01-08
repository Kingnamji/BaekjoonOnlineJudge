# 11758 CCW

def CCW(P1, P2, P3):
    x1, y1 = P2[0]-P1[0], P2[1]-P1[1]
    x2, y2 = P3[0]-P2[0], P3[1]-P2[1]

    outer = x1*y2 - x2*y1
    
    if outer > 0:
        print(1)
    elif outer < 0:
        print(-1)
    elif outer == 0:
        print(0)

P1 = list(map(int, input().split()))
P2 = list(map(int, input().split()))
P3 = list(map(int, input().split()))

CCW(P1, P2, P3)

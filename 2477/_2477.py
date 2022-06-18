# 2477 참외밭
K = int(input()) # 1m^2 당 참외 개수

arr = []
large = [(0,0),(0,0)] #가로, 세로

# 전체 사각형
for i in range(6):
    axis, l = map(int,input().split())
    arr.append((axis,l))
    
    # 가로, 세로 체크
    if axis <= 2: # 동서 => 가로
        axis = 0
    else: # 남북 => 세로
        axis = 1

    # 제일 큰 사각형 찾기
    if l > large[axis][1]:
        large[axis] = (i,l) # 인덱스, 길이 저장
    
    
# 가장 큰 사각형을 이루는 변의 바로 옆
wIdx1, wIdx2 = (large[0][0]-1)%6, (large[0][0]+1)%6
hIdx1, hIdx2 = (large[1][0]-1)%6, (large[1][0]+1)%6
small_w = arr[wIdx1][1] - arr[wIdx2][1]
small_h = arr[hIdx1][1] - arr[hIdx2][1]

sub = abs(small_w * small_h)
all = large[0][1] * large[1][1] 

ans = (all-sub) * K

print(ans)

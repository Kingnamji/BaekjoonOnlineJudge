# -*- coding: utf-8 -*-
"""# 1300

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1waIltd8TRaQcPRtqo9bFWi47tqZnM7-y
"""

# 1300 K번째 수
N = int(input()) # N,N 배열 A 만들 거
k = int(input()) # 일차원으로 오름차순 정렬했을 때 k번째 수 찾기

# 이분 탐색
start = 1
#end = N*N
end = k # k 번째 수는 K 이하다.
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i, N)

    if cnt < k:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1
print(answer)
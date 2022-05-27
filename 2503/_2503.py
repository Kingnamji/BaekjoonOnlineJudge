# 2503 숫자 야구
import sys 
from itertools import permutations

N = int(input())
num = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)) # 순열

for _ in range(N):
    Q, S, B = map(int, sys.stdin.readline().split())
    Q = str(Q)
    pop_cnt = 0

    for i in range(len(num)):
        Strike = 0
        Ball = 0
        i -= pop_cnt # 제거된 경우의 수만큼 줄여줘야 함

        for j in range(3): # 질문한 서로 다른 숫자 세 개
            check_num = int(Q[j]) 
            if check_num in num[i]: # 수가 들어가 있음 
                if j == num[i].index(check_num): # 근데 자리도 같음 => 스트라이크
                    Strike += 1 
                else: # 자리는 다름 => 볼
                    Ball += 1
        if S != Strike or B != Ball: # 스트라이크나 볼 수가 다르면
            num.pop(i) # 삭제
            pop_cnt += 1 # 제거된 경우의 수 

print(len(num)) # 남은 케이스

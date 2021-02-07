# -*- coding: utf-8 -*-
"""# 1016

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A4bJH6Wy75Kv8idobqprBJemTShLJ2Q5
"""

# 1016 제곱 ㄴㄴ 수

def square_nono_number():
    MIN, MAX = map(int, input().split(' '))
    num = [True] * (MAX - MIN + 1) # 제곱으로 나눠지는 수에 대해서 FALSE 처리를 할 것.
    count = 0  # 제곱 ㄴㄴ 수를 세는데 사용.
    N = 1 # 제곱해서 나누기에 사용할 N

    while N * N <= MAX:
        N = N+1 # 2부터 시작 (조건 : 1부터 큰 제곱수)
        square = N * N # 따라서 제곱수는 4부터.
        i = MIN // square
        while square * i <= MAX:
            idx = square * i - MIN # 인덱스이므로 시작하는 숫자만큼 빼줘야함.
            if idx >= 0 and num[idx]: # 인덱스가 0이상이고, 제곱수라고 아직 체크가 안된 경우.
                count += 1 # 제곱수 하나 +
                num[idx] = False # 제곱수라고 확인된 경우 False 값을 갖도록.

            i = i +1  
    print(len(num) - count)

square_nono_number()
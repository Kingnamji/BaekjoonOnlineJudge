# -*- coding: utf-8 -*-
"""# 1065

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TYGEuQ5Q13IyrndXLNIBsOviG6BCGtDq
"""

# 1065 한수
N = int(input())
if N<100:
    print(N) # 99까지는 모두 한수다.
else: # 100이상인경우
    count = 99 # 한수의 개수
    for i in range(100,N+1): # 1이상 N이하의 한수를 따져야함 
        if (i//100 - i%100//10) == (i%100//10 - i%10): # 범위안에서 유일한 네자리수 1000은 한수가 아니다.
            count += 1
    print(count)
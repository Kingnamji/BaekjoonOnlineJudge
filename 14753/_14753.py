# -*- coding: utf-8 -*-
"""# 14753

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1471Ro23ABm6hLYDiCC9N7skGThootM63
"""

# 14753 MultiMax 
N = int(input())
number_list = list(map(int,input().split()))

# 케이스 분리
case = []
number_list.sort()
# 두 수를 선택하는경우 1. 최대인 두 양수의 곱, 2. 최소인 두 음수의 곱
case.append(number_list[0] * number_list[1])
case.append(number_list[N-2] * number_list[N-1])
# 세 수를 선택하는경우 1. 최대인 세 양수의 곱, 2. 최대인 양수 하나와 최소인 두 음수의 곱
case.append(number_list[N-1] * number_list[N-2] * number_list[N-3])
case.append(number_list[0] * number_list[1] * number_list[N-1])
# 그 중에 최대 값 출력
print(max(case))
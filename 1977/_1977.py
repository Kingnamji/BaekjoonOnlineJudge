# -*- coding: utf-8 -*-
"""# 1977

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LfNikYniOvyBW4n2pCNx0W7ZQWJyVyed
"""

# 1977 완전제곱수
square_num = []

M = int(input())
N = int(input())
new_M = M**0.5
new_N = int(N**0.5)

if (new_M % 1) == 0:
    new_M = int(new_M)
else:
    new_M = int(new_M) + 1

square_num = []
for i in range(new_M,new_N+1):
    square_num.append(i**2)

if len(square_num) == 0:
    print(-1)
else:
    print(sum(square_num))
    print(min(square_num))
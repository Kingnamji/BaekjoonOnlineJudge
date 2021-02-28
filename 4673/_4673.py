# -*- coding: utf-8 -*-
"""# 4673

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ajvZHhANgwTphsLYa0iz1CgbXyrwz0oT
"""

# 4673 셀프 넘버

self_num = set(range(1, 10001)) # 1~10000에서 생성자가 있는 숫자를 뺀다.
generated = set()
for i in range(1,10001):
    for j in str(i):
        i += int(j) # 자기 자신 + 각 자리의 수
    generated.add(i) # 생성자가 있는 수 
self_num = self_num - generated  # 생성자가 없는 숫자들의 '집합'

for i in sorted(self_num):
    print(i)
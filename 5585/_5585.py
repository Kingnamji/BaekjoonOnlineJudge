# -*- coding: utf-8 -*-
"""# 5585

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pxtn_R9gGPuZRsx3Hy6Eo8fjWzv55VI9
"""

# 5585 거스름돈
N = int(input())
a = [500, 100, 50, 10, 5, 1]
money = 1000 - N

i = 0
count = 0
while money > 0:
    
    if a[i] <= money:
        count += money // a[i]
        money %= a[i]
        
    i += 1
    

print(count)
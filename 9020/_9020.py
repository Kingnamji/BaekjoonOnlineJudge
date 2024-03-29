# -*- coding: utf-8 -*-
"""# 9020

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G8jsTqhqA32MmW5FtL2zhLKjuf7QZIns
"""

# 9020 골드바흐의 추측
import sys

def isPrime(num):
    i = 2
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        while i <= num**0.5:
            if num % i == 0:
                return False
            i += 1
    
        return True

T = int(input())


for i in range(T):
    N = int(sys.stdin.readline()) 
    
    if (N//2) % 2 == 0:
        a = N // 2 - 1
        b = N // 2 + 1
    else:
        a = N // 2
        b = N // 2

    while a >= 3:
        if isPrime(a) and isPrime(b):
            print(f'{a} {b}')
            break
        else:
            a -= 2
            b += 2


    if (N == 4):
        print('2 2')
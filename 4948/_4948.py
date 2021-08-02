# -*- coding: utf-8 -*-
"""# 4948

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GSnxqWx9CeNZ8Ni0FSEay3buh59M7aMu
"""

# 4948 베르트랑 공준
import sys

def is_prime(n): # 소수 판정
    # 1의 경우는 취급 x
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    
    return True
        
def find_all(): # 범위 내 소수 다 찾기
    primes = []

    for i in range(2,246912):
        if is_prime(i):
            primes.append(i)
    return primes

primes = find_all()

while True:
    n = int(sys.stdin.readline())
    cnt = 0

    if n == 0: # 입력이 0 이면 멈춤
        break

    for i in primes:
        if n < i <= n*2:
            cnt += 1
    print(cnt)

int(2**0.5) + 1
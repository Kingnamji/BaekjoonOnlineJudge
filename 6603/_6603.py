# -*- coding: utf-8 -*-
"""# 6603

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JclseRzXFetW3JSYmQKv0JGAyYgmMrgS
"""

# 6603 로또
from itertools import combinations

def solve():

    while 1:
        lotto = list(map(int, input().split()))

        if lotto[0] == 0: # 입력이 0이면 종료
            break
        
        comb = list(combinations(lotto[1:], 6)) # 조합 만들기
 
        for nums in comb:
            for num in nums:
                print(num, end = ' ')
            print()
        print()

solve()
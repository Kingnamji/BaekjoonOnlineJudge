# -*- coding: utf-8 -*-
"""# 20116

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17l4dKyAlFempchHCN4Z5PZNY3gZzCzsp
"""

# 20116 상자의 균형

def main():
    n, L = map(int,input().split())
    centers = list(map(int, input().split()))
    sum = [0 for _ in range(n)]

    for floor in range(1, n):
        sum[floor] = sum[floor-1] + centers[n-floor]

    for floor in range(n-1, 0, -1):
        if centers[n-floor-1]-L >= (sum[floor] / floor) or (sum[floor] / floor) >= centers[n-floor-1] + L:
            print('unstable') 
            return          
    print('stable')

main()
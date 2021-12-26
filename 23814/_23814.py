# -*- coding: utf-8 -*-
"""# 23814

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-pXcEkHo3U7Yspemxu3wxvRYnufADodZ
"""

# 23814 아 저는 볶음밥이요
D = int(input())

N, M, K = map(int, input().split())

def need(n): # 서비스 받으려면 얼마나 필요한지..
    return D - n%D
    
needN = need(N)
needM = need(M)
now = N//D + M//D + K//D # 군만두 수
now2 = N//D + M//D # 주문 하기 전 군만두 수 
ans = K # 볶음밥 주문 수 

tmp = K%D # 나머지
min_num = min(needN, needM) # 서비스 받기위해 필요한 최소 주문 수
max_num = max(needN, needM) # 서비스 받기위해 필요한 최대 주문 수
if min_num <= tmp: # 나머지가 더 많으면 서비스 받기 가능
    tmp -= min_num
    now += 1
    ans -= min_num

if max_num <= tmp: # 나머지가 더 많으면 서비스 받기 가능
    tmp -= max_num
    now += 1
    ans -= max_num

if ((K-needN-needM)//D + now2 + 2) > now:
    ans = K - needN - needM

print(ans)
# -*- coding: utf-8 -*-
"""# 20546

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gXvphI-lTXvFDEvbhbomQs64fmYllWak
"""

# 20546 기적의 매매법
M = int(input()) # 처음 주어지는 돈
h_money = M 
s_money = M
# 각자의 보유 주식 수
h_stock = 0
s_stock = 0 

daily = list(map(int, input().split())) # 날짜 별 가격
for i in range(3): # 처음 3일은 준현이만 거래
    if (h_money >= daily[i]): # 준현이가 한 주라도 살 수 있다면
        h_num = h_money // daily[i]
        h_stock += h_num
        h_money -= h_num * daily[i]

for i in range(3, 14): # 4일부터 14일까지 둘 다 거래
    # case : 준현
    if (h_money >= daily[i]): # 준현이가 한 주라도 살 수 있다면
        h_num = h_money // daily[i]
        h_stock += h_num
        h_money -= h_num * daily[i]

    # case : 성민
    if (s_money >= daily[i]): # 성민이가 한 주라도 살 수 있다면
        if (daily[i] < daily[i-1]) and (daily[i-1] < daily[i-2]) and (daily[i-2] < daily[i-3]): # 3일째 하락
            s_num = s_money // daily[i]
            s_stock += s_num # 전량 매수
            s_money -= daily[i] * s_num
    if (daily[i] > daily[i-1]) and (daily[i-1] > daily[i-2]) and (daily[i-2] > daily[i-3]): # 3일째 상승
        s_money += s_stock * daily[i] 
        s_stock = 0 # 전량 매도

# 총 가치 계산
h_all = h_money + h_stock * daily[13]
s_all = s_money + s_stock * daily[13]

if (h_all > s_all):
    print('BNP')
elif (h_all < s_all):
    print('TIMING')
else:
    print('SAMESAME')
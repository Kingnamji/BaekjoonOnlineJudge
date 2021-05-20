# -*- coding: utf-8 -*-
"""# 2139

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ywsph7bHR8hLv5aQVl8KZ5Rw-LCu33Yp
"""

# 2139 나는 너가 살아온 날을 알고 있다.
yoon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 윤년
no_yoon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

while 1:
    day, month, year = map(int, input().split())

    if day == 0 and month == 0 and year == 0:
        break

    if year % 4 != 0: # 4로 나누어 떨어지지 않으면
        ans = sum(no_yoon[:month-1]) + day

    else: # 4로 나누어 떨어지면
        if year % 100 == 0: 
            if year % 400 == 0: # 윤년
                ans = sum(yoon[:month-1]) + day
            else:
                ans = sum(no_yoon[:month-1]) + day
        else:
            ans = sum(yoon[:month-1]) + day

    print(ans)
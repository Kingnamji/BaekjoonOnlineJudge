# -*- coding: utf-8 -*-
"""# 1357

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iJp1C5kARFSKY_4qVUUnBlElvrHHtunc
"""

# 1357 뒤집힌 덧셈
# 모든 자리수를 역순으로 만드는 함수 만들기
def Rev(N):
    result = 0
    for i in range(len(N)):
        result += int(N[i]) * (10**i)
    return result

# 입력 받기
X, Y = map(str, input().split())

ans = str(Rev(X) + Rev(Y)) # 결과를 이용하고 다시 한번 문자열로 바꿔주기
ans = Rev(ans)
print(ans)
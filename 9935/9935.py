# 9935 문자열 폭발


sentence = input()
bomb = list(input())
length = len(bomb)

stack = []

for i in range(length-1):
    stack.append(sentence[i])

for i in range(length-1, len(sentence)):
    word = sentence[i]
    stack.append(sentence[i])

    if stack[-length:] == bomb:
        for _ in range(length):
            stack.pop()

if stack:
    for i in stack:
        print(i, end="")
else:
    print('FRULA')

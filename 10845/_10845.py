# -*- coding: utf-8 -*-
"""# 10845

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ThpW7WOhEP9sHkAP2hR3UxrLCHQVt9gX
"""

# 10845 큐
import sys
N = int(input())
queue = []

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
N = int(input())

left = []
for _ in range(N):
    left.append(int(input()))

right = [i for i in(reversed(left))]

max_height = 0
left_num = 0
right_num = 0

for height in left:
    if max_height < height:
        left_num += 1
        max_height = height

max_height = 0
for height in right:
    if max_height < height:
        right_num += 1
        max_height = height

print(left_num)
print(right_num)

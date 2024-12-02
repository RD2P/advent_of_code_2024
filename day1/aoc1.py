left = []
right = []
with open('input.txt') as f:
  for i in f:
    num = i.strip().split('   ')
    left.append(num[0])
    right.append(num[1])

distance = 0
for i,j in zip(sorted(left),sorted(right)):
  distance += abs(int(i)-int(j))

print(distance)
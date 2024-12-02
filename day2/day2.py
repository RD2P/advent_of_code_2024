def check(l):
  # check duplicates
  for n in l:
    if l.count(n) > 1:
      return False
  
  # check rapid change
  for i in range(1, len(l)):
    if abs(l[i] - l[i-1]) > 3:
      return False

  # check increasing/decreasing consistency
  if l[1] - l[0] > 0:
    for i in range(1,len(l)):
      if l[i] - l[i-1] < 0:
        return False
  else:
    for i in range(1,len(l)):
      if l[i] - l[i-1] > 0:
        return False

  return True

safe = 0

with open('input.txt') as f:
  for line in f:
    ls = line.strip().split(' ')   
    l = [int(x) for x in ls]
    if check(l):
      safe += 1

print(safe)
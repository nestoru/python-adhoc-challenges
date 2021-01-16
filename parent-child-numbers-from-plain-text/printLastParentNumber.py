import sys

# create an array from a file to easily test the algo
file_path=sys.argv[1]
parents = []
with open(file_path) as f:
  for line in f:
    parents.append(int(line))

# the following code should print always the greatest parent number
parent_number=0
level=0
level_number=0
#print("i | level | level_number | parent_number")
for i in parents:
  if level == 0:
    if i == parent_number + 1:
      parent_number += 1
    elif i > parent_number + 1:
      pass
    else:
      level += 1
      level_number = i
  else:
    if i == level_number + 1:
      level_number += 1
    elif i > level_number + 1 and i > parent_number + 1:
      pass
    else:
      level -= 1
      level_number = 0
      if level == 0 and i == parent_number + 1:
        parent_number += 1
  #print(str(i) + ' | ' + str(level) + ' | ' + str(level_number) + ' | ' + str(parent_number))
print(parent_number)

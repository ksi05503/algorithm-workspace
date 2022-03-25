size = int(input())


list = []
for i in range(size):
  row = []
  for j in range(size):
    row.append((i+1,j+1))
  list.append(row)
print(list)

# list
# 11 12 13
# 21 22 23
# 31 32 33

n = int(input(""))
numbers = list(map(int,list(input())))

sum = 0
for i in range(0,n):
  sum = sum + numbers[i]

print(sum)
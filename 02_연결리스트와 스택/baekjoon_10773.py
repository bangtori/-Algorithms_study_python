k = int(input())
stack = []

for i in range(k) :
  number = int(input())
  if number != 0 :
    stack.append(number)
  else :
    stack.pop()

print(sum(stack))

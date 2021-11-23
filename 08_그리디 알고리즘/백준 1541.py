import sys
input = sys.stdin.readline

inputExp = input().rstrip().split("-")

resultExp = 0

for index, i in enumerate(inputExp) :
  for j in i.split("+") :
    if index == 0 :
      resultExp += int(j)
    else :
      resultExp -= int(j)

print(resultExp)


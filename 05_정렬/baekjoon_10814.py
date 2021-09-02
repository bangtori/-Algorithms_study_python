import sys
input = sys.stdin.readline

n= int(input().rstrip())
members=[]
for index in range(n):
  age,name = input().rstrip().split()
  members.append((index, age, name))

members.sort(key=lambda member : (int(member[1]),member[0]))

for member in members :
  print(member[1],member[2])


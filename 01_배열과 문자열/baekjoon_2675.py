import sys
input = sys.stdin.readline

t = int(input().rstrip())


for i in range(t) :
  r, s = input().rstrip().split()
  result = ""
  for j in range(len(s)) :
    result += (s[j]*int(r))
  print(result)
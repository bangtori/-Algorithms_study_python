import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
s = list(input().rstrip())

answer = 0
pattern = 0
i = 0

while i < m-2 :
  if s[i] == "I" and s[i+1] == "O" and s[i+2] == "I" :
    pattern +=1
    if pattern == n :
      answer+=1
      pattern-=1
    i +=2
  else :
    pattern = 0
    i +=1 
print(answer)
import sys
input = sys.stdin.readline
from collections import Counter

n= int(input().rstrip())
l = [int(input().rstrip()) for _ in range(n)]

avg = round(sum(l)/n) #두번째 인수로 0을 전달하면 2가 2.0으로 나옴
l.sort()
middle = l[n//2]
rang = l[-1] - l[0]
c = Counter(l)
result = c.most_common(2)

if len(result) == 2 and result[0][1] == result[1][1] :
  mode = result[1][0]
else :
  mode = result[0][0]

print(avg)
print(middle)
print(mode)
print(rang)
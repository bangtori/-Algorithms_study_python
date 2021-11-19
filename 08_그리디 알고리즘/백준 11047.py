import sys
input = sys.stdin.readline

N, K = list(map(int, input().rstrip().split()))

coin = []
for i in range(N) :
  coin.append(int(input().rstrip()))

coin.reverse()
count = 0

for i in coin:
  if K == 0 :
    break
  count += (K // i)
  K %= i

print(count)

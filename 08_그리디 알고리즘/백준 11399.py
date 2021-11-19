import sys
input = sys.stdin.readline

N = int(input().rstrip())
times = list(map(int, input().rstrip().split()))

times.sort()
sum = 0

for index, time in enumerate(times) :
  sum += time*(N-index)

print(sum)
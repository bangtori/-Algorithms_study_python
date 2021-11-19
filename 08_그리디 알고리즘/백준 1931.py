import sys
input = sys.stdin.readline

N = int(input().rstrip())
time_list = []
for i in range(N) :
  time_list.append(list(map(int, input().rstrip().split())))

time_list.sort(key=lambda x: (x[1], x[0]))
count = 0
last_time = 0

for start, end in time_list :
  if last_time <= start :
    count +=1
    last_time = end

print(count)

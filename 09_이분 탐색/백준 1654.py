import sys
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())
lan_length = [int(input()) for _ in range(k)]

start = 1
end = max(lan_length)

while start <= end :
  count = 0
  mid = (start+end)//2
  for i in lan_length :
    count += (i//mid)
  
  if count >= n :
    start = mid+1
  else :
    end=mid-1
  
print(end)
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
tree_length = list(map(int, input().rstrip().split()))

start = 1
end = max(tree_length)

while start <=end :
  sum = 0
  mid = (start+end)//2
  
  for i in tree_length :
    if i >= mid :
      sum += (i-mid)

  if sum >= m :
    start = mid +1
  else :
    end = mid -1
print(end)

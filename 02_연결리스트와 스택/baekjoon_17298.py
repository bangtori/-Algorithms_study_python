import sys
input = sys.stdin.readline

# 시간복잡도(n^2) -> 시간 초과나옴
# n = int(input().rstrip())
# NGE = list(map(int, input().rstrip().split()))
# results = []
# for i in range(0,n) :
#   result = -1
#   for j in range(i+1, n) :
#     if NGE[i]<NGE[j] :
#       result = NGE[j]
#       break
#   results.append(result)
# print(" ".join(map(str,results)))

# 스택을 이용하여 시간복잡도 개선
n = int(input().rstrip())
NGE = list(map(int, input().rstrip().split()))
results = [-1] * n
stack = []
stack.append(0)
for i in range(1,n) :
  while stack and NGE[stack[-1]] < NGE[i]:
    results[stack.pop()] = NGE[i]
  stack.append(i)
print(" ".join(map(str,results)))
import sys
input = sys.stdin.readline

#틀린 풀이
# n = int(input().rstrip())
# a = input().rstrip()
# m = int(input().rstrip())
# m_arr = input().rstrip().replace(" ", "")

# for i in range(m) :
#   if a.find(m_arr[i]) == -1 :
#     print(0)
#   else :
#     print(1)

# set을 이용한 풀이
# set의 in / not in -> O(1)
# list의 in / not in => O(n)
n = int(input())
a = set(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

for i in m_arr:
  if i in a:
    print(1)
  else:
    print(0)


import sys
input = sys.stdin.readline

n = int(input().rstrip())
N_numbers = list(map(int, input().rstrip().split()))
m = int(input().rstrip())
m_numbers = list(map(int, input().rstrip().split()))

n_dic = {}
for i in N_numbers :
  if i not in n_dic :
    n_dic[i] = 1
  else :
    n_dic[i] +=1

N_numbers.sort()
for target in m_numbers :
  left = 0
  right = n-1

  while left<=right :
    mid = int((left+right)/2)
    if N_numbers[mid] == target :
      break
    elif N_numbers[mid] > target :
      right = mid -1
    else :
      left = mid + 1
  
  if N_numbers[mid] == target :
    print(n_dic[target], end=" ")
  else : 
    print(0, end=" ")

#시간 초과
# def binary_search_counting(arr, target):
#   left = 0
#   right = len(arr) -1

#   while left<=right :
#     mid = int((left + right) / 2)
#     if arr[mid] == target :
#       start,end = mid, mid
#       while start-1 >=left:
#         if arr[start-1] != target :
#           break
#         start-=1
#       while end+1 <=right :
#         if arr[end+1] != target :
#           break
#         end +=1
#       return end-start+1
#     elif arr[mid] > target :
#       right = mid -1
#     else :
#       left = mid + 1
  
#   return 0


# result = []
# N_numbers.sort()
# for i in m_numbers :
#   result.append(binary_search_counting(N_numbers, i))

# for i in result :
#   print(i, end=" ")
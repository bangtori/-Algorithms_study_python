from collections import Counter

str = input().upper()
c = Counter(str)
result = c.most_common(2)
# if len(result) == 1 :
#   print(result[0][0])
# else : 
if len(result) == 2 and result[0][1] == result[1][1] :
  print("?")
else :
  print(result[0][0]) 

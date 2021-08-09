n = int(input())
results = []

for i in range(0,n) :
  sum = 0
  preScore = 0
  testCase = list(input(""))
  for j in testCase :
    if j == 'O' :
      preScore = preScore + 1
      sum = sum + preScore
    else : # X일경우
       preScore = 0
  
  results.append(sum)

for score in results :
  print(score)

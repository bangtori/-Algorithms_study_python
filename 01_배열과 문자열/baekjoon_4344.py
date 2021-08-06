c = int(input())
results = []

for i in range(0,c) :
  inputs = list(map(int, input().split()))
  n = inputs[0]
  scores = inputs[1:]
  avg = sum(scores)/len(scores)
  cnt = 0
  for score in scores :
    if score > avg :
      cnt = cnt +1
  results.append(cnt/len(scores) * 100)

for result in results :
  print("%.3f"%result+"%")



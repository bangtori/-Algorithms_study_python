import sys
input = sys.stdin.readline

n = int(input().rstrip())
word_list = []

for _ in range(n) :
  word = str(input().rstrip())
  word_list.append((word,len(word)))

word_list = list(set(word_list))

word_list.sort(key=lambda word :(word[1],word[0]))

for word in word_list :
  print(word[0])






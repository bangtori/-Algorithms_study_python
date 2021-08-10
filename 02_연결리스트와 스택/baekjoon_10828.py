#파이썬 시간 초과 해결하는 방법 
#input -> sys.stdin.readline
#단 문자열 입력을 받을 시 개행문자도 포함되기 때문에 rstrip() 사용
import sys
input = sys.stdin.readline

class Stack :
  def __init__(self) -> None:
      self.stack = []
  
  def empty(self) :
    if not self.stack : #비어 있음
       return 1
    else :
      return 0
  
  def size(self) :
    return len(self.stack)

  def push(self, x) :
    self.stack.append(x)

  def pop(self) :
    if self.empty() :
      return -1
    else :
      return self.stack.pop()
  
  def top(self) :
    if self.empty() :
      return -1
    else :
      return self.stack[self.size() -1]

s = Stack()
n = int(input())
for i in range(0,n) :
  inputs = input().rstrip()
  if len(inputs.split())==1 :
    command = inputs
  else :
    command, item = inputs.split()
  
  if command == "push" :
    s.push(item)
  elif command == "pop" :
    print(s.pop())
  elif command == "top" :
    print(s.top())
  elif command == "size" :
    print(s.size())
  elif command == "empty" :
    print(s.empty())
# class Node :
#   def __init__ (self, data, prev=None, next=None) :
#     self.data = data
#     self.prev = prev
#     self.next = next
  
# class DoublyLinkedList:
#   def __init__(self) :
#     self.head = None
#   def insert(self, index, node) :
#     cur = self.head
#     prevNode = None
#     curIndex = 0
#     if index == 0 :
#       if self.head :
#         nextNode = self.head
#         nextNode.prev = node
#         self.head = node
#         self.head.next = nextNode
#       else :
#         self.head = node
#     else :
#       while curIndex < index :
#         if cur : 
#           prevNode = cur
#           cur = cur.next
#         else:
#           break;
#         curIndex +=1
#       if curIndex == index :
#         node.next = cur
#         node.prev = prevNode
#         cur.prev = node
#         prevNode.next = node
#       else : 
#         return -1
#   def delete(self,index) :
#     curIndex = 0
#     cur = self.head
#     prevNode = None
#     nextNode = self.head.next
#     if index == 0 :
#       self.head = nextNode
#     else :
#       while curIndex < index :
#         if cur.next :
#           prevNode = cur
#           cur = nextNode
#           nextNode = nextNode.next
#         else :
#           break
#         curIndex +=1
#       if curIndex  == index :
#         prevNode.next = nextNode
#         nextNode.prev = prevNode
#       else :
#         return -1

import sys
input = sys.stdin.readline

str = input().rstrip()
n = len(str)
cursor = n
m = int(input().rstrip())
for i in range(0,m) :
  inputs = input().rstrip()
  if len(inputs.split())==1 :
    command = inputs
  else :
    command, item = inputs.split()

  if command == "L" :
    if cursor > 0 :
      cursor-=1
  elif command == "D" :
    if cursor < n :
      cursor += 1
  elif command == "B" :
    if cursor > 0 :
      str[cursor-1]
      cursor -=1
      n-=1
  elif command == "P" :
    str.insert(cursor, item)
    cursor +=1
    n += 1

print(str)
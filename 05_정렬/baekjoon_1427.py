import sys
input = sys.stdin.readline

n= input().rstrip()
n= list(n)
n.sort(reverse=True)
print("".join(n))
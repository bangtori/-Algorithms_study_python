import sys
input = sys.stdin.readline

a = list(map(int, input().rstrip()[::-1].split()))
print(max(a))
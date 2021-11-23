import sys
from typing import Mapping
input = sys.stdin.readline

N = int(input().rstrip())
road_length = list(map(int, input().rstrip().split()))
oil_price = list(map(int, input().rstrip().split()))

result = 0

min_price = oil_price[0]

for index, road in enumerate(road_length) :
  if min_price > oil_price[index] :
    min_price = oil_price[index]
  result += (min_price * road)

print(result)
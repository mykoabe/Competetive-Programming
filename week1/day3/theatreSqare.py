from math import ceil
n,m,a = map(int, input().split())
m = ceil(m/a)
n = ceil(n/a)
print(int(m * n))
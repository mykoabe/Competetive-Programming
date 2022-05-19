def count(n):
    if n < 2:
        return 1
    return count(n//2) * 2 + 1
 
def calc(n, x):
    if x == 0:
        return 0
    if n < 2:
        return n
    m = count(n//2)
    if x <= m:
        return calc(n//2, x)
    if x == m + 1:
        return n//2 + n%2
    return n//2 + n % 2 + calc(n//2, x - m - 1)
 
n, l, r = map(int, input().split())
print(calc(n, r) - calc(n, l - 1))

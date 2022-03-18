import heapq
m = []
N = int(input())
di = dict()
for i in range(N):
    b = input().split()
    if b[0] == '1':
        b = int(b[1])
        di[b] = 0
        heapq.heappush(m,b)
    elif b[0] == '2':
        b = int(b[1])
        di[b] = 1
    else:
        while di[m[0]] == 1:
            heapq.heappop(m)
        print(m[0])
print(di)
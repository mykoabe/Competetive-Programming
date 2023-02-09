n, d = map(int, input().split())
s = input()
dp = "0"*d
i, j = 0, 0
if dp not in s:
    while i < n-1:
        if s[i] == "1":
            i += d
            j += 1
        else:
            i -= 1
    print(j)
else:
    print(-1)

# if dp in s:
#     print(-1)
# else:
#     while i<len()-1 :
#         if arr[i]=="1":
#             i+=y
#             j+=1
#         else:
#             i-=1
#     print(j)

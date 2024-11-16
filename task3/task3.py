n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
max = a[n-1]
maxn = 1
for i in range(n-2, -1, -1):
    if(a[i] * (n - i) > max):
        max = a[i] * (n - 1)
        maxn = n - i
print(max // maxn, maxn)



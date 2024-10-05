m, n, t = int(input()), int(input()), int(input())
sum = 0
cnt = 0
while((sum + (2 * m) + (2 * n) - 4) <= t):
    sum = sum + (2 * m) + (2 * n) - 4
    n -= 2
    m -= 2
    cnt += 1
print(cnt)

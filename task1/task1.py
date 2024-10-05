a, b, n, m = int(input()), int(input()), int(input()), int(input())
a1, b1, a2, b2 = n + (n - 1) * a, n + (n + 1) * a, m + (m - 1) * b, m + (m + 1) * b
if(a1 > a2):
    a1, b1, a2, b2 = a2, b2, a1, b1
if(a1 == a2):
    if(b1 == a1 or b2 == a1):
        print(a1, a1)
    else:
        print(a1, min(b1, b2))
else:
    if(a2 > b1):
        print(-1)
    elif(a2 == b1):
        print(a2, a2)
    elif(b2 <= b1):
        print(a2, b2)
    else:
        print(a2, b1)

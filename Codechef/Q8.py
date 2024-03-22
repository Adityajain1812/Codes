T = int(input())
for tc in range(T):
    X , Y = map(int , input().split())
    c = X + Y
    if c > 6:
        print("YES")
    else:
        print("NO")
        
t = int(input())
for _ in range(t):
    A , B = map(int , input().split())
    if A > B:
        print('A')
    else:
        print('B')

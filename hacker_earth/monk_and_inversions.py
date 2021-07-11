for _ in range(int(input())):
    c = 0
    m = list()
    n = int(input())
    for _ in range(n):
        m.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(n):
            for p in range(n):
                for q in range(n):
                    if i<=p and j<=q and m[i][j] > m[p][q]:
                        c+=1
    print(c)
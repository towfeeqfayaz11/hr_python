# find second largest no in an array

if __name__ == '__main__':
    solution 1:
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(n-1,-1,-1):
        if arr[i]>arr[i-1]:
            print(arr[i-1])
            break
    

    # solution 2:
    i = int(input())
    lis = list(map(int,input().strip().split()))[:i]
    z = max(lis)
    while max(lis) == z:
        lis.remove(max(lis))
    print(max(lis))



    # solution 3:
    n = int(input())
    arr = sorted(list(set(map(int,input().split()))))
    print(arr[-2])
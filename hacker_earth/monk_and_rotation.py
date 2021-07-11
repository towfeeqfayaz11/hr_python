# question : top rotate an array to right by k elements   (rotate_array_right)

# Input:
# The first line will consists of one integer T denoting the number of test cases.
# For each test case:
# 1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation.
# 2) The next line consists of N space separated integers , denoting the elements of the array A.
# Output:
# Print the required array.



# solutions

# solution 1
for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    k = k % n  # if rotate value is greater than array size, array will be unaffected (so to counter that we use modulus)
    arr = arr[-k:]+arr[:-k]
    print(*arr)


# solution 2 (partially submitted (TLE) )
# def array_rotate(arr, k):
#     for _ in range(k):
#         tmp = arr[-1]
#         arr.pop()
#         arr.insert(0,tmp)
# for _ in range(int(input())):
#     n,k = map(int,input().split())
#     arr = list(map(int,input().split()))
#     if k > 0:
#         array_rotate(arr, k)
#     print(*arr)



# solution 3
# from collections import deque
# for _ in range(int(input())):
#     n,k = map(int,input().split())
#     d = deque(map(int,input().split()))
#     d.rotate(k)
#     print(*d)




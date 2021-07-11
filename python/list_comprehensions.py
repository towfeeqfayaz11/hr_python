# Problem: List Comprehensions - easy


#solution(1):
x, y, z, n = int(input()), int(input()), int(input()), int(input())        # for taking input from n lines
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])


#solution(2):
x, y, z, n = (int(input()) for _ in range(4))    # for taking inout from n lines
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])



NOTE: 
x, y, z, n = int(input()), int(input()), int(input()), int(input())    # this will take input from 4 lines and assign accordingly to variables
x, y, z, n = (int(input()) for _ in range(4))   # this will take input from 4 lines and assign accordingly to variables
x, y, z, n = [int(input()) for _ in range(4)]   # this will take input from 4 lines and assign accordingly to variables


x, y, z, n = map(int, input().split())          # this will take input from single line (will assign 4 inputs to variable on left side accordingly)
x, y, z, n = [int(i) for i in input().split()]  # takes input seperated by space from a single line
x, y, z, n = (int(_) for _ in input().split())  # takes input seperated by space from a single line
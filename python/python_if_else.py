# Problem: Python If-Else   => easy


#solution(1):
n = int(input().strip())
if (n % 2 != 0):
    print("Weird")
elif (n % 2 == 0) and n in range(2,6):
    print("Not Weird")
elif (n % 2 == 0) and n in range(6,21):
    print("Weird")
elif (n % 2 == 0) and n > 20:
    print("Not Weird")




#solution(2):
n = int(input().strip())
if (n % 2 != 0) or ((n % 2 == 0) and n in range(6,21)):
    print("Weird")
elif ((n % 2 == 0) and n in range(2,6)) or ((n % 2 == 0) and n > 20):
    print("Not Weird")




#solution(3):
n = int(input().strip())
if n%2==0 and (n in range(2,6) or n>20):
    print("Not",end=' ')
print("Weird")



#solution(4):
n = int(input().strip())
check = {True: "Not Weird", False: "Weird"}
print(check[n%2==0 and (n in range(2,6) or n>20)])
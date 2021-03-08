# Problem: Loops    => easy


#solution(1):
print(*[num**2 for num in range(n)], sep='\n')    # note here if * is not used then list will be printed in singel line despite using sep='\n'
                                                  # using * unpacks the list first and then prints each element of unpacked list on new line
                                       # This is an arbitrary argument list. It works by expanding a list into a sequence of positional parameters by using the * operator.



#solution(2):
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(pow(i,2))
        #print(i**2)


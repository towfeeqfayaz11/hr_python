# fin the count of occurance of a substring in a string


def count_substring(string, sub_string):
    #len([i for i in range(len(s)) if s[i:i+len(b)] == b])
    count = 0
    pos = 0
    while(True):
       pos = string.find(sub_string , pos)
       if pos > -1:
           count = count + 1
           pos += 1
       else:
           break
    return count



# method 1:
def count_substring(string, sub_string):
    n1 = len(string)
    n2 =len(sub_string)
    c = 0
    for i in range(n1-n2+1):
        if sub_string == string[i:i+n2]:
            c+=1
    return c
        
 


# method 2:   
def count_substring(string, sub_string):
	count = 0
    pos = 0
    while(True):
       pos = string.find(sub_string , pos)
       if pos > -1:
           count = count + 1
           pos += 1
       else:
           break
    return count


# method 3:
def count_substring(string, sub_string):
    return len([1 for i in range(len(string) - len(sub_string)) if string[i:i+len(sub_string)] == sub_string])


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
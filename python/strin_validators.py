# input: is a string

# Output Format:
# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.



# solution 1:
if __name__ == '__main__':
    s = input()
    list1 = [False] * 5
    for i in s:
        if i.isalnum() and list1[0] == False:
            list1[0] = True
        if i.isalpha() and list1[1] == False:
            list1[1] = True
        if i.isdigit() and list1[2] == False:
            list1[2] = True
        if i.islower() and list1[3] == False:
            list1[3] = True
        if i.isupper() and list1[4] == False:
            list1[4] = True
    for i in list1:
        print(i)



# solution 2:
s = input()
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))



# solution 3:     # slower code (the eval statement is recompiled on each iteration)
s = input()
for test in ('isalnum','isalpha','isdigit','islower','isupper'):
    print(any(eval("c."+test+"()") for c in s))


# solution 4:    # this is faster compared to above
# Note: c.isalnum()  === str.alnum(c)
# Reason: Remember that class methods are just functions with an object as the first parameter - true in any OO language but directly visible and usable from Python.
for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print(any(method(c) for c in s))
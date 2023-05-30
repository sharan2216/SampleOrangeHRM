# # using Split method---------
def palindrome(s):
    temp = s[::-1]
    if temp == s:
        print("Yes Palindrome")
    else:
        print("Not a Plindrome")


s = "nitin"
palindrome(s)


# using indexing:-------

def palindrome2(s):
    size = len(s)
    for i in range(size):
        if s[i] != s[size - 1]:
            return False
        return True


s = "nitin"
palindrome2(s)


# Inbuilt function Reversed

def palindrome3(s):
    reverse_s = reversed(s)
    # print(reverse_s)

    for i in reverse_s:
        temp_s = ''.join(reversed(s))
        print(temp_s)
        if s == temp_s:
            return True
        return False


s = "nitin"
palindrome3(s)


# using Number (Integer):-

def palindrome_num(n):
    temp = n # 1456
    rev_no = 0
    while temp > 0:  #1456 >0
        digit = temp % 10 # 6 --remainder value
        rev_no = rev_no * 10 + digit #-- 0*10+6 = 6
        temp = temp // 10 # 1456/10 = 145.6(145  coz it ignore the values after decimal value)

    if n == rev_no:
        print("Palindrome Number")

    else:
        print("Not a Palindrome Number")


n = 123454321
palindrome_num(n)

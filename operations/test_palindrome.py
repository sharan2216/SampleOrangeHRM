# # using Split method---------
# def palindrome(s):
#     temp = s[::-1]
#     if temp == s:
#         print("Yes Palindrome")
#     else:
#         print("Not a Plindrome")
#
# s="nitin"
# palindrome(s)

# using indexing:-------

def palindrome2(s):
    size = len(s)
    for i in range(size):
        if s[i] != s[size-1]:
            return False
        return True


s = "nitin"
palindrome2(s)

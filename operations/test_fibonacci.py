# using Java ------------
# def fibonacci(n):
#     a = 0
#     b = 1
#     while (b < n):
#         print(b)
#         c = a + b
#         a = b
#         b = c
#
#
# fibonacci(50)
# print("-----------------------------------")


# 2nd way using For loop in python :----------

def fibonacci2(n):

    n1,n2 = 0,1
    if n==1:
        print(n)
    else:
        print(n1)
        print(n2)
    for i in range(2, n):
        sum = n1 + n2
        print(sum)
        n1 = n2
        n2 = sum


fibonacci2(10)

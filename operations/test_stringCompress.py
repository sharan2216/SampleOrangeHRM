def compress(s):
    n = len(s)
    count = 0
    new_s =''

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            count = count + 1
        else:
            new_s = new_s + s[i] + str(count)
            count = 1

        new_s = new_s + s[n - 1] + str(count)
        return new_s


s = "aabbcccddeeeiiii"
print(compress(s))

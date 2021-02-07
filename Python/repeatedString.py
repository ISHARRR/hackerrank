def repeatedString(s, n):

    # new_string = n * s
    print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))

repeatedString('aba', 10000000)



# new_string = n * s
# return (new_string[:n].count('a'))

def fac(n):
    if n == 0:
        return 1

    while n > 0:
        factorial = n * fac(n - 1)
        print(factorial)
        return factorial


# You can play around with your solution from within this block.
print("fac({}) = {}".format(31, fac(31)))

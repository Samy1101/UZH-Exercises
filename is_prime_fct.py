
# gibt nur 2.75 Punkte, Fehler noch nicht gefunden

def is_prime(n):
    if n == 1:
        return "1 is the multiplicative identity."

    for a in range (2, int(n**(1/2))+1):
        if n % a == 0:
            b = n // a
            return "%d is not a prime number (%d * %d = %d)" %(n, a,b, n)

    return "%d is prime" % n

print(is_prime(3))
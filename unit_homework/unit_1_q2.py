
def isprime(n):
    factors = []
    for d in range(2,n):
        if n%d == 0:
            factors.append(d)
    return len(factors) == 0

primes = []

for n in range (2,2001):
    if isprime(n):
        primes.append(n)

print(sum(primes))



# % will give me remainders; if there are remainders, then it's not divisible
# a prime number has only two factors: 1 and itself
# Create a list of factors for each number. If the length is 2, then it is prime

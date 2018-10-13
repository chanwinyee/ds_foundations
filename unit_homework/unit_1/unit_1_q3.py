# Find the sum of all the multiples of 3 and 5 below 1,000

def divisible_by_three_or_five(n):
    if (n%3 == 0 or  n%5 == 0):
        return True

total = 0

for n in range(1,1001):
    if divisible_by_three_or_five(n):
        total = total + n

print(total)

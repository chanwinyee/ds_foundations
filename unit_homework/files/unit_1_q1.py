# the product of two three-digit numbers will have 6 digits, so a Palindrome will not have an odd one in the middle

def isPalindrome(test):
#    print (test[0:3])
#    print (test[::-1][0:3])
    return test[0:3] == test[::-1][0:3]

# print isPalindrome('123321')
test=set()
palindromes = []

for x in range(100,1000):
    for y in range (100,1000):
        test.add(int(x)*int(y))

for z in test:
    if isPalindrome(str(z)):
        palindromes.append(z)

print max(palindromes)

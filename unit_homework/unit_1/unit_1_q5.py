def fizzbuzz_operator(x):
    if x%3 == 0 and x%5 == 0:
        print('Fizzbuzz')
    elif x%3 == 0 or x%5 == 0:
        print('Fizz')
    else:
        pass

fizzbuzz_operator(9)
fizzbuzz_operator(10)
fizzbuzz_operator(45)
fizzbuzz_operator(19)

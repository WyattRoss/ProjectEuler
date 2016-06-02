import fibo
fip = fibo.fib(4000000)
print sum(filter(lambda x: x % 2 == 0, fip))
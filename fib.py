
# Classic rescursive fibnacci calculator
# fib(5) = fib(4) + fib(3)
# So
# fib(5) = (fib(3) + fib(2)) + (fib(2) + fib(1))
def recursive_fibonacci(n):
   if n <= 1:
       return n
   else:
       return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

# Variables are defined like this. Notice how we don't care about types.
foo = 15
bar = 25
print(f"This code was just run. Foo is {foo} and bar is {bar} and foo/bar is {foo/bar}");   
# Notice that we divided two integers and got a float.
# Also - the string formatting  stuff is just beautiful.

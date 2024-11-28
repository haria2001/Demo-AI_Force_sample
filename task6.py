# Display the Fibonacci series with recursion and without recursion

# with recursion 
def fibonacci_series(n):
    if n<=1:
        return n
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)
    
n = fibonacci_series(11)
print(n)


# without recursion 
n = 4
a,b = 0,1 
for i in range(n):
    print(a, end='')
    a,b = b, a+b
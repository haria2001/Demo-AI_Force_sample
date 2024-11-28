# Find the factorial of a number with recursion and without recursion

# with recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
num = factorial(5)
print(num)

# with out recursion

n = 7
factorial = 1
for i in range(1,n+1):
    factorial *= i
print(n)
        

# Print all the factors of a given number

def factorial(n):
    for i in range(1, n+1):
        if n%i == 0:
            print(i)
    return ''
n = factorial(4)
print(n)


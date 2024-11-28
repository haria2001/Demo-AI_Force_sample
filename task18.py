# Print all the primes in the given range using Sieve of Eratosthenes

start = int(input("enter the starting range: "))
end = int(input("enter the ending range: "))

primes = [True] * (end + 1)
primes[0] = primes[1] = False

p = 2
while p * p <= end:
    if primes[p]:
        for i in range(p * p, end + 1, p):
            primes[i] = False
    p += 1
for num in range(max(2, start), end + 1):
    if primes[num]:
        print(num, end=" ")

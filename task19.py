# Improve the timing of the prime number printing program

start = 1
end = 99

if start < 2:
    start = 2
    
for num in range(start, end +1):
    is_prime = True
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break 
    if is_prime:
        print(num)

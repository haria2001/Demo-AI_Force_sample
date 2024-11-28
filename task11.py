# Print the list of perfect numbers in the given range

start = 1 
end = 100
perfect_numbers = []

for num in range(start, end+1):
    sum = 0
    
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        perfect_numbers.append(num)
print(perfect_numbers)


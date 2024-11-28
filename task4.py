# Print all the numbers divisible by a given number in the range

start_number = 1
end_number = 50
divisor = 3
l1 = []
for i in range (start_number, end_number+1):
    if i % divisor == 0:
        l1.append(i)
print("Divisible number with 3 are :", l1)
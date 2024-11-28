# Print all the Armstrong numbers in the given range
start = int(input("enter the starting number: "))
end = int(input("enter the ending number: "))

for num in range(start, end+1):
    temp = num 
    result = 0
    n = len(str(num))

    while temp > 0:
        digit = temp % 10
        result += digit ** n
        temp //= 10
    if result == num:
        print(num)
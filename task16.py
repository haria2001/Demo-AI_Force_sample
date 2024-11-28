# Find if the given number is an Armstrong number

num = int(input("Enter a number: "))
temp = num 
result = 0
n = len(str(num))

while temp>0:
    digit = temp%10
    result += digit ** n
    temp //= 10
if result == num:
    print(f"{num} is an Amstrong number")
else:
    print(f"{num} is not an Amstrong number")
# Convert the given decimal number to binary

decimal = 13
binary = ''
if decimal == 0:
    binary = "0"
    
while decimal > 0:
    rem = decimal % 2
    binary = str(rem) + binary
    decimal = decimal // 2

print(binary)

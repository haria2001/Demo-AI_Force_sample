# Convert the given decimal number to hexadecimal

decimal_number = 333
hex_char = "0123456789ABCDEF"
hexadecimal_number = ""
if decimal_number == 0:
    hexadecimal_number = "0"
    
while decimal_number > 0:
    rem = decimal_number % 16
    hexadecimal_number = hex_char[rem] + hexadecimal_number
    decimal_number = decimal_number // 16
print(hexadecimal_number)    
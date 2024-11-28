#  Print the list of prime numbers in the given range

r1 = 1
r2 = 100
l1 = []
for num in range(r1, r2+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                l1.append(i)
                break
        else:
            print(num, end = '')
  
    
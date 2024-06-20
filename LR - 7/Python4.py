num = int(input())
n = 0
for i in range(2, n // 2+1):
    if (num % i == 0):
        n = n+1
if (n <= 0):
    print('Число - простое')
else:
    print('Число - не простое')
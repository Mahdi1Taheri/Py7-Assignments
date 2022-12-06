n = int(input("Enter the n number of pascal's triangle: "))

for i in range(n):
    print(' ' * (n - i), end='')
    print(*(map(str, str(11 ** i))))
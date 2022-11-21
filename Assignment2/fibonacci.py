# Fibonacci Series.

lst = [0,1]

nth = int(input("How many elements of the Fibonacci sequence will be shown?: "))

if nth > 2:
    for i in range(2,nth):
        fibo = lst[i - 1] + lst[i -2]
        lst.append(fibo)
    print(lst)

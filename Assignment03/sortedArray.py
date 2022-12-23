array = input("enter your numbers with space between them: ").split(" ")

if array != sorted(array):
    print("this array is NOT sorted.❌")
else:
    print("this array is sorted!✔")

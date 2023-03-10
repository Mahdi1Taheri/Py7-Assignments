def is_symmetric(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    
    return True

arr = input("enter your array with a space between every number: ")
arr.split(" ")
print(is_symmetric(arr))
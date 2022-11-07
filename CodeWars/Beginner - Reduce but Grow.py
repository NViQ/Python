def grow(arr):
    n = 1
    for i in arr:
        n *= i
    print(n)

grow([1,2,3])
def binary_array_to_number(arr):
    bin_string = ''.join(map(str, arr))
    print(int(bin_string, base =2))

    # return int("".join(map(str, arr)), 2)


binary_array_to_number([0, 1, 0, 1])
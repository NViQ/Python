def sum_two_smallest_numbers(n):
    m = sorted(n)
    print(sum([m[0], m[1]]))
    # return sum(sorted(n)[:2])

sum_two_smallest_numbers([55,33,88,11])

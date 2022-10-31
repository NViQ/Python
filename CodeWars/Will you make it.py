def zero_fuel(dist, mpg, fuel):
    if dist <= mpg * fuel:
        print(True)
    else:
        print(False)


zero_fuel(100, 50, 1)
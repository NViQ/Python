def baum_sweet(val):
    def baum_sweet():
        yield 1;
        i = 0;
        while True:
            i += 1
            yield not any(map(lambda j: len(j) % 2, bin(i).split('1')))


baum_sweet(12)
print([1,1,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0])
print(bin(21))
print((bin(21).count('0')) % 2)
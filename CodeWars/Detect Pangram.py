def is_pangram(s):
    m = 0
    for i in set(s.lower()):
        if i.isalpha():
            m += 1
    if m == 26:
        print(True)
    else:
        print(False)


is_pangram('The quick, brown fox jumps over the lazy dog!')#, True)
is_pangram('1bcdefghijklmnopqrstuvwxyz')#, False)


def is_isogram(string):
    print(True if len(set(string.lower())) == len(string.lower()) else False)

# def is_isogram(string):
#     return len(string) == len(set(string.lower()))


is_isogram("Dermatoglyphics")#, True )
is_isogram("isogram")#, True )
is_isogram("aba")#, False, "same chars may not be adjacent" )
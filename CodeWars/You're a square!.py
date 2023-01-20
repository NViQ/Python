def is_square(n):
    if n == 0 or n > 0 and n % (n ** 0.5) == 0:
        print(True)
    else:
        print(False)
   #if b.typ:
    #   print(True)



#is_square(-1)#, False, "-1: Negative numbers cannot be square numbers")
#is_square( 0)#, True, "0 is a square number (0 * 0)")
is_square( 3)#, False, "3 is not a square number")
is_square( 4)#, True, "4 is a square number (2 * 2)")
is_square(25)#, True, "25 is a square number (5 * 5)")
is_square(26)#, False, "26 is not a square number")
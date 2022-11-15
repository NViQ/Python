def sum_str(a, b):
    if a == '' and b == '':
        return str(0)
    else:
        return str(int(a)+int(b)) if a and b else a or b




sum_str("4", "5")#, "9")
sum_str("34", "5")#, "39")
sum_str("", "55")#, "39")
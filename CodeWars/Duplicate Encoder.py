def duplicate_encode(word):
    l = []
    n = word.lower()
    for i in n:
        if n.count(i)>1:
            l.append(')')
        else:
            l.append('(')
    print(''.join(l))
    print('(((())())((((')

    # return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

duplicate_encode("lGZEWtMWTnVIS")

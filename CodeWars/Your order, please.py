def order(sentence):
    dict_s = {}
    l = []
    for i in sentence.split():
        for n in i:
            if n.isdigit() == True:
                dict_s[n] = i
    for key, value in sorted(dict_s.items()):
        l.append(value)
    print(' '.join(l))

    # return ' '.join(sorted(sentence.split(), key=lambda w: sorted(w)))

order("4of Fo1r pe6ople g3ood th5e the2")
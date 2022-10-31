def find_uniq(arr):
    for i in arr:
        for n in arr:
            if i !=n and arr.count(i)>1:
                print(n)

    # a, b = set(arr)
    # return a if arr.count(a) == 1 else b

    # a = sorted(arr)
    # return a[0] if a[0] != a[1] else a[-1]
find_uniq([ 3, 10, 3, 3, 3 ])


def reverse_words(text):
    # if text.count(' ') >= 1:
    #     b = []
    #     for i in text.split():
    #         b.append(i[::-1])
    #     sp = ' ' * int(int(text.count(' ')) / int(len(text.split()) - 1))
    #     print(sp.join(b))
    # else:
    #     print(text[::-1])
    print(' '.join(s[::-1] for s in text.split(' ')))


reverse_words("stressed  desserts")
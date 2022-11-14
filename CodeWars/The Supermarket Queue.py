def queue_time(cust, n):
    if len(cust) == 0:
        return 0
    elif n > len(cust):
        return max(cust)
    elif n == 1:
        return sum(cust)
    elif len(cust) > n:
        l = []
        for i in cust[:n]:
            l.append(i)
        for m in cust[n:]:
            l.sort()
            b = list(map(lambda x: x + m, l))
            l[0] = min(b)
        return max(l)


# def queue_time(customers, n):
#     l=[0]*n
#     for i in customers:
#         l[l.index(min(l))]+=i
#     return max(l)


# queue_time([26, 2, 2, 3, 8, 31, 3, 45, 48, 43], 3)#: 81 should equal 79
# queue_time([27, 19, 33, 5, 42, 46, 26, 32, 15, 21, 29, 40, 1, 13, 7, 27, 26, 16, 34], 5)#: 129 should equal 108
# queue_time([], 1)#, 0, "wrong answer for case with an empty queue")
# queue_time([5], 1)#, 5, "wrong answer for a single person in the queue")
# queue_time([2], 5)#, 2, "wrong answer for a single person in the queue")
# queue_time([1, 2, 3, 4, 5], 100)#, 5, "wrong answer for a case with a large number of tills")
# queue_time([2, 2, 3, 3, 4, 4], 2)#, 9, "wrong answer for a case with two tills")
# queue_time([1, 2, 3, 4, 5], 2)#, 9, "wrong answer for a single till")
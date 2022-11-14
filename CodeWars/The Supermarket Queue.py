def queue_time(arr):

    print(sorted(set(arr))[-2])

    # if len(cust) == 0:
    #     return 0
    # elif n > len(cust):
    #     return max(cust)
    # elif n == 1:
    #     return sum(cust)
    # elif len(cust) > n:
    #     b = 0
    #     l = []
    #     # while b < n:
    #     for i in range(0,n):
    #
    #     l.append(sum(cust[b::n]))
    #     b += 1
    #     print(max(l))

queue_time([1, 2, 5, 7, 9, 9])
# queue_time([26, 2, 2, 3, 8, 31, 3, 45, 48, 43], 3)#: 81 should equal 79
# queue_time([27, 19, 33, 5, 42, 46, 26, 32, 15, 21, 29, 40, 1, 13, 7, 27, 26, 16, 34], 5)#: 129 should equal 108
# queue_time([], 1)#, 0, "wrong answer for case with an empty queue")
# queue_time([5], 1)#, 5, "wrong answer for a single person in the queue")
# queue_time([2], 5)#, 2, "wrong answer for a single person in the queue")
# queue_time([1, 2, 3, 4, 5], 100)#, 5, "wrong answer for a case with a large number of tills")
# queue_time([2, 2, 3, 3, 4, 4], 2)#, 9, "wrong answer for a case with two tills")
# queue_time([1, 2, 3, 4, 5], 2)#, 9, "wrong answer for a single till")
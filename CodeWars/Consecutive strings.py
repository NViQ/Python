def longest_consec(strarr, k):
    n = 0
    con_list = ['o']
    if len(strarr) >= k > 0:
        while len(strarr) >= k > 0:
            if len(''.join(strarr[n:k])) > len(con_list[0]):
                con_list[0] = (''.join(strarr[n:k]))
            n +=1
            k +=1
        print(con_list)
    else:
        print('')


longest_consec(["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2) #, "wlwsasphmxxowiaxujylentrklctozmymu")
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)#, "")
longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3)#, "ixoyx3452zzzzzzzzzzzz"


# def longest_consec(s, k):
#     return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""

# def longest_consec(strarr, k):
#     if (len(strarr) == 0 or k <= 0) or len(strarr) < k:
#         return ""
#     lst = [''.join(strarr[i:i+k]) for i in xrange(len(strarr))]
#     return max(lst, key= lambda x: len(x))
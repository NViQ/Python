def solution(s):
    l = []
    for i in s:
        if i.isupper():
            v = i.replace(i, ' '+i)
            l.append(v)
        else:
            l.append(i)
    print(''.join(l))


# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)




solution("problemUseCompanyCaseCompanyCaseAsk")#, "problem Use  CompanyCaseCompany CaseAsk")
solution("ableWorldNumber WorldNumberTakeWoman")#, "able World Number  WorldNumberTakeWoman")
solution("publicGiveGiveTryGreatOther")#
solution("earlyNounsNextNounsNextSame")#
solution("findNewNewComeNumber")#
solution("bigLongThinkTimeThinkTimePublic")#
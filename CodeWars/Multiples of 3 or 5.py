def solution(num):
    s2 = set()
    if num > 3:
        for i in range(0,num,3):
            s2.add(i)
        if num > 5:
            for j in range(0,num,5):
                s2.add(j)
        print(sum(s2))
    else:
        print(0)

# return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)



solution(4)#, 3)
solution(6)#, 8)
solution(16)#, 60)
solution(3)#, 0)
solution(5)#, 3)
solution(15)#, 45)
solution(0)#, 0)
solution(-1)#, 0)
solution(200)#, 9168)
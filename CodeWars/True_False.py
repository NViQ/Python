"""
Write a function that validates the correctness of parentheses sequence.
Input data is sttring, containing a parentheses. Output - boolean value.
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""
# def brackets (parenth):
#     print(parenth.count('(') == parenth.count(')'))


# brackets("(())((()())())")
# brackets("(")
# brackets(")(()))")
# brackets('(())((()())())')

"""2. Given an array of integers, return indices of the two numbers such that they add up to a specific target.
5 6 2 4
8
=> 1 2"""

# def int_sum(nums, targ):
#     for i in nums:
#         for m in nums:
#             if i + m == targ:
#                 print(nums.index(i), nums.index(m))
#
# int_sum([5,6,2,4], 8)

"""1. Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !"""

def pig_it(text):
    мфк = []

    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)

    print(' '.join(res))

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !"""
# s = 'django'
# print(s[0])
# print(s[-1])
# print(s[:4])
# print(s[1:4])
# print(s[4:])
# print(s[::-1])


# lst = [3, 7, [1, 4, 'hello']]
# lst[2][2] = 'goodbye'
# print(lst)

# d1 = {'simple_key': 'hello'}
# d2 = {'k1': {'k2': 'hello'}}
# d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
# print(d1['simple_key'])
# print(d2['k1']['k2'])
# print(d3['k1'][0]['nest_key'][1][0])
# d4 = d3.copy()
# d4['k1'][0]['nest_key'][1][0] = 10
# print(d4['k1'][0]['nest_key'][1][0])


# AND = 1>2 and 2>3
# OR = 3>2 or 4>3
# multiple = 1 > 2  or 2 == 2 or 1 < 2

# print(AND)
# print(OR)
# print(multiple)


# if 1<3:
#     print('First block')
#     if 20>3:
#         print('second block')
    

# if 1>4:
#     print('in iff')
# elif 1<4:
#     print('in elif')
# else:
#     print('in else')


# item = {'sam': 1, 'frank': 2}
# for d in item:
#     print(d)
# for k in item:
#     print(item[k])


# mypairs = [(1,5), (2,6), (3,7)]
# for tup1, tup2 in mypairs:
#     print(tup1)
#     # print(tup2)



# i = 5
# while i < 5:
#     print(i)
#     i += 1

# print(i)


# x = [1, 2, 3, 4]
# out = []
# for num in x:
#     out.append(num**2)
    
# print(out)    



# def addNum(num1, num2):
#     return num1 + num2

# result = addNum(2, 3)
# print(result)



# st = 'tweet go! #sports'
# print(st.split('#'))



# x = range(6)


def arrayCheck(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False
 

#173
# def myfunction():
#     k = input('Enter number -- >')
#     if k == '':
#         return 0
#     else:
#         c = int(k)
#         return  c + myfunction()
# print(myfunction())

#174
# def myfuntion(a,b):
#     if b == 0:
#         return a
#     else:
#         c = a % b
#         return myfuntion(b,c)
# a = int(input('Enter number -- > '))
# b = int(input('Enter number -- > '))
# print(myfuntion(a,b))

#175
# def myfunction(a):
#     if a == 1:
#         return 1
#     else:
#         return str(a%2) + str(myfunction(a // 2))
# a = int(input('Enter number -- > '))
# print(myfunction(a)[::-1])

#176


# def myfunction(text,i):
#     mydict = {
#     'A' : 'Alpha',
#     'B' : 'Bravo',
#     'C' : 'Charlie',
#     'D' : 'Delta',
#     'E' : 'Echo',
#     'F' : 'Foxtrot',
#     'G' : 'Golf',
#     'H' : 'Hotel',
#     'I' : 'India',
#     'J' : 'Juliet',
#     'K' : 'Kilo',
#     'L' : 'Lima',
#     'M' : 'Mike',
#     'N' : 'November',
#     'O' : 'Oscar',
#     'P' : 'Papa',
#     'Q' : 'Quebec',
#     'R' : 'Romeo',
#     'S' : 'Sierra',
#     'T' : 'Tango',
#     'U' : 'Uniform',
#     'V' : 'Victor',
#     'W' : 'Whiskey',
#     'X' : 'Xray',
#     'Y' : 'Yankee',
#     'Z' : 'Zulu',
#     }
#     if i + 1  > len(text):
#         return ''
#     else:
#         i += 1
#         return mydict[str(text[i-1])] + ' ' + myfunction(text,i) 
# text = input('Enter text -- >')
# i = 0
# print(myfunction(text,i))

#177
# import math
# def myfunction(text,count):
#     mydict = {
#     'M' : 1000,
#     'D' : 500,
#     'C' : 100,
#     'L' : 50,
#     'X' : 10,
#     'V' : 5,
#     'I' : 1
#     }
#     if count == len(text):
#         return 0
#     else:
#         if count == 0:
#             return mydict[text[count]] + myfunction(text,count+1)
#         else:
#             if mydict[text[count]] > mydict[text[count - 1]]:
#                 c = mydict[text[count]] * -1
#                 return c + myfunction(text,count+1)
#             else :
#                 return mydict[text[count]] + myfunction(text,count+1)
# count = 0
# text = input('Enter text -- > ')
# print(abs(myfunction(text,count)))

#178
# def myfunction(text):
#     if 1 >= len(text):
#         return True
#     else:
#         return text[0] == text[len(text) - 1] and myfunction(text[1:len(text)-1])
        
# text = input('Enter text')
# count = 0
# b = True
# print(myfunction(text))

#179
# def myfuntion(n,guess):
#     if abs(guess ** 2 - n) < 0.0000000000000001:
#         return guess
#     else:
#         return myfuntion(n,(guess + n/guess)/2)
# n = int(input('Enter number --> '))
# guess = 1
# print(myfuntion(n,guess))

#184
# def func(mylist):
#     if len(mylist) == 0:
#         return []
#     elif type(mylist[0]) == list:
#         return func(mylist[0]) + func(mylist[1:])
#     else:
#         return [mylist[0]] + func(mylist[1:])
# print(func([1,[2,3],[4,[5,[6,7]]],[[[8],9],[10]]]))

#185 ????
# def myfunction(mylist): 
#     if mylist == []:
#         return []
#     elif mylist[1] != 0:
#         mylist[1] -= 1
#         return mylist[0] + myfunction(mylist)
#     else:
#             return myfunction(mylist[2:])    
# mylist = ['A',1,'B',1,'A',1,'B',1]
# print(myfunction(mylist))
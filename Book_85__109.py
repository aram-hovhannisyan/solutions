#85
# import math
# def nerqnadziq(a,b):
#     c = a ** 2 + b ** 2
#     return int(math.sqrt(c))
# errankyan_koxm1 = int(input('Nermuceq arajin koxmi erkarutyuny -- > '))
# errankyan_koxm2 = int(input('Nermuceq erkrord koxmi erkarutyuny -- > '))
# print(nerqnadziq(errankyan_koxm1,errankyan_koxm2))

#86
# import math
# chanaparh = int(input('Chanaparhi erkarutyuny -- >')) 
# def taxi(a):
#     bazain = 4
#     avel = bazain * 6.25 / 100
#     if a <= 6:
#         return bazain
#     if a > 6:
#         pox = (a - 6) * 1000/140
        
#         # print(math.ceil(pox))
#         yndhanur = bazain + math.floor(pox) * avel
#         return yndhanur
# print(taxi(chanaparh))

#87
# import math
# def araqum(a):
#     araji_apranq = 10.95
#     mnacac = 2.95
#     if a == 1 :
#         return araji_apranq
#     elif a > 1:
#         yndhanur = araji_apranq + (a-1) * mnacac
#         return round(yndhanur,2)
#     else :
#         print('Qanak chka')
# apranqi_qanak = int(input('Qani hat apranqe harkavor araqel  -- >'))
# print(araqum(apranqi_qanak))

#88
# def mediana(a,b,c):
#     maximum = max(a,b,c)
#     minimum = min(a,b,c)
#     if a != maximum and a != minimum:
#         return a 
#     elif b != maximum and b != minimum:
#         return b
#     elif c != maximum and c != minimum:
#         return c 
    
# first = int(input('First number -- > '))
# second = int(input('Second number -- > '))
# third = int(input('Third number -- > '))
# print(mediana(first,second,third))

#89
# def myfunction(a):
    
#     mydict = {
#         '1' : 'One',
#         '2' : 'Two',
#         '3' : 'Three',
#         '4' : 'Four',
#         '5' : 'Five',
#         '6' : 'Six',
#         '7' : 'Seven',
#         '8' : 'Eight',
#         '9' : 'Nine',
#         '10' : 'Ten',
#         '11' : 'Eleven',
#         '12' : 'Twelve'   
#     }
#     for i in mydict:
#         if i == a:
#             return mydict.get(f'{i}')
# number = input('Number from 1 to 12 -- > ')
# print(myfunction(number))

#90

# def myfunction():
#     arajin = 'A partridge in a pear tree'
#     esiminch = ''

#     erkrord = 'And a partridge in a pear tree'
#     mydict = {
#         'first' : '',
#         'second' : 'Two turtle doves,',
#         'third' : 'Three French hens,',
#         'fourth' : 'Four calling birds',
#         'fifth' : 'Five golden rings',
#         'sixth' : 'Six geese a-laying',
#         'seventh' : 'Seven swans a-swimming',
#         'eight' : 'Eight maids a-milking',
#         'ninth' : 'Nine ladies dancing',
#         'tenth' : 'Ten lords a-leaping',
#         'eleventh' : 'Eleven pipers piping',
#         'twelfth' : 'Twelve drummers drumming'
#     } 
#     for i in mydict:
        
#         text = f'On the {i} day of Christmas \nmy true love sent to me: \n'

#         if i == 'first':
#             verjnakan = text + arajin + '\n\n'
        
#         elif i == 'second':

#             # esiminch = ''
#             esiminch = esiminch + mydict.get(f'{i}') + '\n' + erkrord
#             verjnakan = verjnakan + text  + esiminch + '\n\n'
        
#         else:
#              esiminch = mydict.get(f'{i}') + '\n' + esiminch 


#              verjnakan = verjnakan + text  + esiminch + '\n\n'
             
#     return verjnakan

        
# print(myfunction())

#91
# def ordinalDate( d, m, y ):
#     if  y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
#         leap = True
#     else:
#         leap = False
#     amisner = [31,28+leap,31, 30,31,30, 31,31,30, 31,30,31]
#     md = 0
#     for i in range(m-1):
        
#         md += amisner[i]
#     return md + d
# d = int(input('Or -- >'))
# m = int(input('Amis -- >'))
# y = int(input('Tari -- >'))

# print(ordinalDate(d,m,y))

#92

# d = int(input('OR -- > '))
# y = int(input('TARI -- > '))
# d1 = d + 10
# def georgDate(d,y):
#     if  y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
#         leap = True
#     else:
#         leap = False
#     c = 0
#     amisner = [31,28+leap,31, 30,31,30, 31,31,30, 31,30,31]
#     for i in amisner:
#         if d > i:
#             d = d - i
#             c += 1
#         else:
#             c = c + 1
#             break
    
#     return d , c
# print(georgDate(d,y))
# print(georgDate(d1,y))

#93
# import math
# print(4 * '\t' + 'dasda')
# s = input('Text == > ')
# w = int(input('Laynutyun == > '))
# def myfunction(s,w):
#     text = ' '
    
#     if len(s) >= w:
#         return s
#     else:
#         c = round(abs((len(s) - w)) // 2)
#         return c * text + s        
# print(myfunction(s,w))

#94
# koxm1 = int(input('Araji koxm -- > '))
# koxm2 = int(input('Erkrord koxm -- > '))
# koxm3 = int(input('Errord koxm -- > '))
# def myfunction(koxm1,koxm2,koxm3):
#     maximum = max(koxm1,koxm2,koxm3)
#     if maximum >= koxm1 + koxm2 or maximum >= koxm1 + koxm3 or maximum >= koxm2 + koxm3:
#         return False
#     else:
#         return True
# print(myfunction(koxm1,koxm2,koxm3))


#95 
# def myfunction(text):
#     nshanner = '?!'
#     for i in range(0,len(text)-1):
#         if text[i] in  nshanner:
#             text = text.replace(text[i+1],text[i+1].upper())
#     return text
# print(myfunction(input('Enter text -- > ').capitalize()))

# 96
# text = input('Enter text -- >')
# def myfunctio(text):
#     tver = '1234567890'
#     count = 0
#     for i in range(0,len(text)):
#         if text[i] in tver:
#             count += 1
#     if count == len(text):
#         return True
#     else: 
#         return False
# print(myfunctio(text))

# 97
# text = input('Enter text -- > ')
# def myfunction(text):
#     for i in range(0,len(text)):
#         if text[i] == '+' or text[i] =='-':
#             return 1
#         elif text[i] == '*' or text[i] == '/':
#             return 2
#         elif text[i] == '^':
#             return 3
# print(myfunction(text))

#98
# number = int(input('Enter number'))
# def myfunction(number):
#     count = 0
#     for i in range(1,number+1):
#         if number % i == 0:
#             count += 1    
#     if count == 2:
#         return True
#     else:
#         return False
# print(myfunction(number))

#99

# number = int(input('Enter number'))
# def myfunction(number):
#     count = 0
#     for i in range(1,number+1):
#         if number % i == 0:
#             count += 1    
#     if count == 2:
#         return True
#     else:
#         return False
# if myfunction(number):
#     print(myfunction(number))
# else:
#     while True:
#         number += 1
#         myfunction(number)
#         if myfunction(number):
#             print(number)
#             break
#         else:
#             continue

#100
# import random
# def password():
#     x = random.randint(7,10)
#     k = 0
#     password =''
#     while k <= x:
#         password =password + chr(random.randint(33,126))
#         k += 1
#     return password
# print(password())

#101
# import random
# def hamar():
#     tarer = 'QWERTYUIOPASDFGHJKLZXCVBNM'
#     newlist = []
#     hamaranish = ''
#     for i in range(0,len(tarer)):
#         newlist.append(tarer[i])
#     for i in range(0,7):
#         if i <= 3:
#             hamaranish += str(random.randint(0,9))
#         else:
#             hamaranish += random.choice(newlist)
#     return hamaranish
# print(hamar())
    
#102

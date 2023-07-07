#63
# x = int(input('Nermuceq tiv --> '))
# s = 0
# b = 0
# if x == 0:
#     print('ERROR')
# while( x != 0) :
#     s = s + x
#     b +=1
#     x = int(input('Nermuceq tiv --> '))
#     if x == 0 :
#         break
# d  = s / b
# print(d)

#64
# b = 4.95
# print(f'Skzbnakan\tZexch\tVerjnakan')
# for  i in range(0,5):
#     skzbnakan = b * 100 / 60
#     zexch = skzbnakan - b
#     print(f'{round(skzbnakan,2)}$\t\t{round(zexch,2)}$\t\t{round(b,2)}$')
#     b = b + 5

#65
# print('Celsus --> Fareyheyt\tF=(C X 9/5) + 32')
# print(f'Celsus\t\tFarreyn')
# for i in range(0,101,10):
#     C = i
#     F = (C * 9/5) + 32
#     print(f'{C}\t\t{F}')

#66

# x = input('Nermuceq gumar --> ')
# sum = 0
# while(True):
#     if x.isdigit():
#         d = int(x)
#         sum = sum + d
#         c = sum // 5
#         b = sum % 5
#         x = input('Nermuceq gumar --> ')
#     else : 
#         break
# if b < 2.5:
#     print(c * 5)
# elif b > 2.5:
#     print((c * 5) + 5)

#67
# import math
# c = 0
# while(True):
#     X = input('X kordinat-> ')
#     Y = input('Y kordinat --> ')
#     X_1 = input('X kordinat --> ')
#     Y_1 = input('Y kordinat --> ')
#     x = int(X)
#     y = int(Y)
#     x_1 = int(X_1)
#     y_1 = int(Y_1)
#     c = c + math.sqrt((x - x_1)**2 + (y - y_1)**2)
#     while(True):
#         X_2 = input('X kordinat --> ')
#         if X_2 == ' ':
#             break
#         Y_2 = input('Y kordinat --> ')
#         x_2 = int(X_2)
#         y_2 = int(Y_2)
#         c = c + math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)
#         x_1 = x_2
#         y_1 = y_2    
#     c = c + math.sqrt((x - x_1)**2 + (y - y_1)**2)
#     break
# print(f'c = {c}')

#68
# sum = 0
# c = 0
# while(True):
#     gnahatakan = input('Nermuceq gnahatakany -->')
#     if gnahatakan == 'A' or gnahatakan == 'A+':
#         sum  = sum + 4
#         c += 1
#     elif gnahatakan == 'A-':
#         sum = sum + 3.7
#         c += 1
#     elif gnahatakan == 'B+':
#         sum = sum + 3.3
#         c += 1
#     elif gnahatakan == 'B':
#         sum = sum + 3
#         c += 1
#     elif gnahatakan == 'B-':
#         sum = sum + 2.7
#         c += 1 
#     elif gnahatakan == 'C+':
#         sum = sum + 2.3
#         c += 1
#     elif gnahatakan == 'C':
#         sum = sum + 2
#         c += 1
#     elif gnahatakan == 'C-':
#         sum = sum + 1.7
#         c += 1
#     elif gnahatakan == 'D+':
#         sum = sum + 1.3
#         c += 1
#     elif gnahatakan == 'D':
#         sum = sum + 1
#         c += 1
#     elif gnahatakan == 'F':
#         c += 1
#     x = input('Sharunakel YES/NO -->')
#     if x == 'Yes':
#         continue
#     elif x == 'No':
#         break
# print(sum/c)
        
#69
# sum = 0
# while(True):
#     x = input('Age = ')
#     if x == ' ':
#         break
#     elif int(x) <= 2:
#         sum = sum + 0
#     elif int(x) >= 3 and int(x) < 12:
#         sum = sum + 14
#     elif int(x)  >= 12 and int(x) < 65:
#         sum = sum + 23
#     elif int(x) >= 65 :
#         sum = sum + 18
# print(sum)

#70
# c = 0
# while(True):
#     number = input('Number --> ')
#     for i in range(0,len(number)):
#         c = c + int(number[i])
#     if c % 2 == 0 :
#         print('Zuyg')
#     else :
#         print('Kent')

#71
# x3 = 4
# p =3
# for i in range(0,15):
    
#     p = p + 4 /((x3-2)*(x3-1)*x3)-4/(x3*(x3+1)*(x3+2))
#     x3 += 2 
# print(p)

#72
# for i in range(1,101):
#     if i == 1 :
#         print(i)
#     elif i % 3 == 0:
#         if i % 5 == 0 :
#             print('FIZZ-BUZZ')
#         else:
#             print('FIZZ')
#     elif i % 5 == 0:
#         if i % 3 ==0 :
#             print('FIZZ-BUZZ')
#         else :
#             print('BUZZ')
#     else:
#         print(i)

#73 
# chars = 'A-Z'
# text = input('Enter text - > ')
# for i in range(0,len(text)):
#     if text[i] in chars
#     print(chars[chars.index(text[i]) + 3])
#74
x = int(input('Number '))
guess = x / 2
while abs(guess ** 2 - x) > 0.001:
    guess = (guess + x / guess) /2
print(guess)

#75
# text = input('Text -->')
# x1 = text[::-1]
# while(True):
#     if text == x1:
#         print('Polindrom')
#     else :
#         print('Polindrom chi')
#     text = input('Text --> ')

#76 
# text = input('Text --> ')
# count = 0
# chars = '!@#$%^&*() _-+=.,:;'
# while count != len(text):
#     if text[count] in chars:
#         text = text.replace(text[count],'')
        
        
#     else:
#         count += 1
# print(text)
# x = text[::-1]
# if text == x :
#     print('Polidrom')
# else :
#     print('No polidrome')

#77
# print(f"{' ': >2}",end="")
# for i in range(1,11):
#     print(f'{i: >5}',end="")
# print('\n')
# for i in range(1,11):
#     print(f"{i:>2}",end="")
#     for j in range(1,11):
#         print(f"{i*j: >5}",end="")
#     print('\n')

#78

# while True:
#     x = int(input('Number -- > '))
#     if x > 0 :
#         for i in range(1,x+1):
#             print(i)
#     else :
#         break

#79
# x = int(input('Number 1 --> '))
# y = int(input('Number 2 --> '))
# d = min(x,y)
# b = True
# while (b):
#     if x % d == 0 :
#         if y % d == 0:
#             b = False
#         else:
#              d -= 1
#     else :
#         d -= 1            
# print(d)

#80
# x = int(input('Number -- > '))
# factor = 2
# while factor <= x :
#     if x % factor == 0:
#         print(factor)
#         x = x / factor
#     else :
#         factor += 1 

#81
# text = input('2 akan hamakarg --> ')
# count = 0
# astichan = len(text)-1
# for i in range (0,len(text)):
#     if text[i] == '0':
#         astichan -= 1    
#     elif text[i] == '1':
#         count = count + (2 ** astichan)
#         astichan -= 1
# print(count)

#82
# b = ''
# x = int(input('Number -->'))
# while  x > 0:
#     b = str(x % 2) + b
#     x = x // 2
# print(b)

#83
# from itertools import count
# import random
# x = random.randint(1,100)
# print(x)
# max = x
# count =  0
# for i in range(1,100):
#     x = random.randint(1,100)
#     if x > max :
#         max = x
#         count += 1
#         print(f'{max} --> Poxvec')
#     else :
#         print(x)
# print(f'Maximal arjeqnery 1-100 mijakayqum\npopoxutyunneri qanak --> {count}')        
    
#84
# import random
# kopek = ['O','R']
# R = 0
# O = 0
# count = 0
# count_1 = 0
# x = input('Do you want to play YES/NO --> ')
# while x == 'YES':
#     while True:
#         k = random.choice(kopek)
#         if k == 'R':
#             R += 1
#             O = 0
#             count += 1

#         elif k == 'O':
#             O += 1
#             R = 0
#             count += 1

#         print(k,end=' ')
        
#         if R == 3:
#             break
#         elif O == 3:
#             break
#     print(f'{count}\n')
#     count_1 += 1
#     x = input('Do you want to play YES/NO --> ')
# print(f'{count_1}')    


    

    
        






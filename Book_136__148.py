#136
# def reverselookup():
#     mydict = {}
#     while True:
#         k = input('Enter Key -- >')
#         v = input('Enter Value -- >')
#         if k == ' ' or v == ' ':
#             break
#         else:
#             mydict[k] = v
#     return mydict
# print(reverselookup())        


#137 
# import random
# def qcel():
#     a = random.randint(1,6)
#     b = random.randint(1,6)
#     return a+b
# mydict = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
# for i in range(0,1000):
#     c = qcel()
#     mydict[c] += 1
# print(mydict)

#138
# text = input('Enter text -- >')
# mydict = {
#     1 : ['?',',','.','!',':'],
#     2 : ['A','B','C'],
#     3 : ['D','E','F'],
#     4 : ['G','H','I'],
#     5 : ['J','K','L'],
#     6 : ['M','N','O'],
#     7 : ['P','Q','R','S'],
#     8 : ['T','U','V'],
#     9 : ['W','X','Y','Z'],
#     0 : ' '
# }
# for i in range(0,len(text)):
#     c = text[i]
#     for j in mydict:
#         if c in mydict[j] :
#             k = mydict[j].index(c) + 1
#             print(str(j)*k,end='')

#139
# mydict = {
#     'A': '.–',
#     'B': '–...',
#     'C': '–.–.',
#     'D': '–..',
#     'E': '.',
#     'F': '..–.',
#     'G': '-–.',
#     'H': '....',
#     'I': '..',
#     'J': '.---',
#     'K': '-.-',
#     'L': '.–..',
#     'M': '--',
#     'N': '=',
#     'O': '---',
#     'P': '.--.',
#     'Q': '--.-',
#     'R': '.–.',
#     'S': '...',
#     'T': '–',
#     'U': '..–',
#     'V': '...-',
#     'W': '==',
#     'X': '-..-',
#     'Y': '-.--',
#     'Z': '--..',
#     '0' : '-----',
#     '1' : '.----',
#     '2' : '..---',
#     '3' : '...--',
#     '4' : '....-',
#     '5' : '.....',
#     '6' : '-....',
#     '7' : '--...',
#     '8' : '---..',
#     '9' : '----.'
# }
# text = input('Enter text -- > ')
# for i in range(0,len(text)):
#     c = text[i]
#     for j in mydict:
#         if c == j:
#             print(mydict[j],end='')

#140
# mydict = {
#     'Ньюфаундленд' : 'A',
#     'Новая Шотландия' :'B',
#     'Остров Принца Эдуарда': 'C',
#     'Нью-Брансуик' : 'E',
#     'Квебек' :['G', 'H','J'],
#     'Онтарио'  :['K', 'L', 'M',' N' ,'P'],
#     'Манитоба' : 'R',
#     'Саскачеван': 'S',
#     'Альберта' : 'T',
#     'Британская Колумбия' :'V',
#     'Нунавут' :'X',
#     'Северо-Западные территории' :'X',
#     'Юкон': 'Y'
# }
# while True:
#     text = input('Enter text -- > ')
#     if len(text) == 6:
#         if text[0].isalpha() and text[1].isdigit():
#             break
# for i in mydict:
#     if text[0] in mydict[i]:
#         print(i)

#141
# dict1 = {
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four',
#     5: 'five',
#     6: 'six',
#     7: 'seven',
#     8: 'eight',
#     9: 'nine',
# }
# dict2 = {
#     10:'ten',
#     20 :'twenty',
#     30 :'thirty',
#     40 :'fourty',
#     50 :'fifty',
#     60 :'sixty',
#     70 :'seventy',
#     80 :'eighty',
#     90 :'ninety',
#     100 :'hundred'
# }
# dict3 = {
#     11: 'elevan',
#     12: 'twelve',
#     13: 'thirteen',
#     14: 'fourteen',
#     15: 'fifteen',
#     16: 'sixteen',
#     17: 'seventeen',
#     18: 'eighteen',
#     19: 'nineteen'
# }
# mylist=[]
# verjnakan = ''
# number = (input('Enter number -- > '))
# if len(number) == 3:
#     tiv = int(number) // 100
#     verjnakan = verjnakan + dict1[tiv] +' '+ 'hundred'
#     k = int(number) - tiv * 100
#     if k < 20 and k > 10:
#         verjnakan = verjnakan + dict3[k]
#     elif k < 10:
#         verjnakan = verjnakan + ' ' + dict1[k]
#     else :
#         verjnakan = verjnakan + ' ' + dict2[(k // 10)*10] +' ' + dict1[(k-(k//10)*10)]
# elif len(number) == 2:
#     if int(number) >= 20 and int(number)%10 != 0:
#         # tiv = int(number) //10
#         verjnakan = verjnakan + dict2[(int(number) //10)*10] + ' ' + dict1[(int(number)-(int(number) //10)*10)]
#     elif int(number) >= 20 and int(number)% 10 == 0:
#         verjnakan = verjnakan + dict2[int(number)]
# elif len(number) == 1:
#     verjnakan = verjnakan + dict1[int(number)]
# print(verjnakan)

#142
# text = input('Enter text -- > ')
# mydict = {}
# for i in range(0,len(text)):
#     mydict[text[i]] = '1'
# count = 0
# for i in mydict:
#     count += 1
# print(count)


#143
# bar1 = input('Enter text -- > ')
# bar2 = input('Enter text -- > ')
# mylist1 =[]
# mylist2 =[]
# count = 0
# if len(bar1) != len(bar2):
#     print(False)
# else:
#     for i in range(0,len(bar1)):
#         mylist1.append(bar1[i])
#     for i in range(0,len(bar2)):
#         mylist2.append(bar2[i])
#     for i in mylist1:
#         if i in mylist2:
#             count += 1    
#     if count == len(mylist2):
#         print(True)
#     else:
#         print(False)
#144
# bar1 = input('Enter text -- > ')
# bar2 = input('Enter text -- > ')
# mylist1 =[]
# mylist2 =[]
# count = 0

# for i in range(0,len(bar1)):
#     if bar1[i] == ' ' or bar1[i] == '?':
#         continue
    
#     mylist1.append(bar1[i])
# for i in range(0,len(bar2)):
#     if bar2[i] == ' ' or bar2[i] == '?':
#         continue    
#     mylist2.append(bar2[i])
# for i in mylist1:
#     if i in mylist2:
#         count += 1    
# if count == len(mylist2):
#     print(True)
# else:
#     print(False)
#145
# text = input('Enter text -- >')
# mydict = {
#     1 : ['A', 'E', 'I', 'L', 'N', 'O','R', 'S', 'T', 'U'],
#     2 :['D','G'],
#     3 : ['B', 'C', 'M' ,'P'],
#     4 : ['F','H','V','W' ,'Y'],
#     5 : 'K',
#     8 : ['J','X'],
#     10: ['Q' , 'Z']
#     }
# count = 0
# for i in range(0,len(text)):
#     c = text[i]
#     for j in mydict:
#         if c in mydict[j]:
#             count += j
# print(count)
#146
# import random
# def myfunction():
#     mydict ={}
#     mylist = []
#     for i in range(0,5):
#         mylist.append(random.randint(1,16))
#     mydict['B'] = mylist
#     mylist = []
#     for i in range(0,5):
#         mylist.append(random.randint(16,30))
#     mydict['I'] = mylist
#     mylist = []
#     for i in range(0,5):
#         mylist.append(random.randint(30,45))
#     mydict['N'] = mylist
#     mylist = []
#     for i in range(0,5):
#         mylist.append(random.randint(45,60))
#     mydict['G'] = mylist
#     mylist = []
#     for i in range(0,5):
#         mylist.append(random.randint(60,75))
#     mydict['O'] = mylist
#     mylist = []
#     for i in mydict.values():
#         print(i)
#147
# import random
# def myfunction():
#     mydict ={}
#     mylist = []
#     for i in range(0,5):
#         mylist.append(random.randint(1,16))
#     mydict['B'] = mylist
#     mylist = []
#     for i in range(0,5):
#         mylist.append(random.randint(16,30))
#     mydict['I'] = mylist
#     mylist = []
#     for i in range(0,5):
#         mylist.append(random.randint(30,45))
#     mydict['N'] = mylist
#     mylist = []
#     for i in range(0,5):
#         mylist.append(random.randint(45,60))
#     mydict['G'] = mylist
#     mylist = []
#     for i in range(0,5):
#         mylist.append(random.randint(60,75))
#     mydict['O'] = mylist
#     mylist = []
#     return mydict
# winlist = []
# newdict = myfunction()
# for i in range(0,5):
#     winlist.append(random.randint(1,75))
# index = 0
# kroxlist = []
# for i in newdict.values():
#     if winlist[index] in i:
#         kroxlist.append(i.index(winlist[index]))
#         index += 1
#     else:
#         break
# print(newdict.values())
# print(winlist)
# print(kroxlist)

#148

    


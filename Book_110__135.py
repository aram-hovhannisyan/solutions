#110
# mylist = []
# while True:
#     x = int(input('Number -- >'))
#     if x == 0:
#         break
#     else:
#         mylist.append(x)
# mylist.sort()
# print(mylist)

#111
# mylist = []
# while True:
#     x = int(input('Number -- >'))
#     if x == 0:
#         break
#     else:
#         mylist.append(x)
# mylist.sort(reverse=True)
# print(mylist)

#112
# mylist = []
# while True:
#     x = int(input('Numbers --> '))
#     if x == 0:
#         if len(mylist) <= 4:
#             print('ERROR')
#         else :
#             break 
#     mylist.append(x)
# mylist.sort()
# print(mylist[0],mylist[-1]) 

#113
# mylist = ['first','second','third','first','first','third','fourth','second']

# for i in mylist[::]:
#     if mylist.count(i) > 1:
#         mylist.remove(i)
# print(mylist)
    
#114

# mylist = []
# while True:
#     x = input('Numbers --> ')
#     if x == ' ':
#         break
#     else:
#         mylist.append(x)            
# mylist1 = []
# for i in range(0,len(mylist)):
#     mylist1.append(int(mylist[i]))
# mylist1.sort()
# print(mylist1)

#115
# x = int(input('Number --> '))
# mylist = []
# for i in range(1,x+1):
#     if x % i == 0:
#         mylist.append(i)
    
# print(mylist)

#116
# mylist = []
# t = 0
# for i in range(1,10000+1):
#     if i == 1:
#         mylist.append(i)
#     for j in range(1,i):
#         if i % j == 0:
#             t = t + j
#     if t == i:
#         mylist.append(i)
#     t = 0
# print(mylist)

#117
# x = input('Text -- > ')
# mylist = []
# mylist.append(x.split(' '))
# print(mylist[0])

#118
# mylist = []
# x = input('Text -- > ')
# txt = x.split()
# for i in range(0,len(txt)):
#     mylist.append(txt[i])
# mylist.reverse()
# if mylist == txt :
#     print('polindrome')
# else:
#     print('Non polindrome')

#119
# mylist = []
# mylist1 = []
# cacr = []
# havasar = []
# bardzr = []
# t = 0

# while True:
#     x = input('Numbers --> ')
#     if x == ' ':
#         break
#     else:
#         mylist.append(x) 
# for i in range(0,len(mylist)):
#     mylist1.append(int(mylist[i]))
#     t += int(mylist[i])
# s = t / len(mylist1)
# for i in range(0,len(mylist1)):
#     if mylist1[i] < s :
#         cacr.append(mylist1[i])
#     elif mylist1[i] > s:
#         bardzr.append(mylist1[i])
#     else :
#         havasar.append(mylist1[i])
# print(f'{s}\n{cacr}\n{havasar}\n{bardzr}')

#120
# mylist = []
# mylist1 = []
# while True :
#     x = input('Text --> ')
#     if x == ' ':
#         break
#     else:

#         mylist.append(x)

# for  i in range(0,len(mylist)):
#     if i == 0 :
#         print(mylist[i])
#         mylist1.append(mylist[i])
#     else:
#         print(f'{mylist1[::]} and {mylist[i]}')

#         mylist1.append(mylist[i])
# print(mylist1)

#121
# import random 
# bilet = []
# for i in range(0,6):
#     x = random.randint(1,49)
#     if bilet.count(x)> 1:
#         continue
#     else:
#         bilet.append(x)
# print(bilet)


#122 ??
#123??




    
           






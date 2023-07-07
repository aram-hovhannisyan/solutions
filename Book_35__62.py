#35
# a = int(input('Nermuceq tiv -->'))
# if a % 2 == 0 :
#     print('Zuyg')
# else :
#     print('Kent')

#36
# mard = int(input('Mardu tariq--> '))
# if mard == 10.5 :
#     print('Shant tariq --> 1')
# elif (mard == 21) :
#         print('Shan tariq --> 2')
# elif (mard > 21) :
#         print(2 + (mard - 21) // 4)
# else : print('sxal tiv ')  

#37
# let = input('Nermuceq tarr--> ')
# b = ['a','e','i','o','u']
# if let in b : print('Dzaynavor')
# elif let == 'y': print('Ham kara lini dzaynavor hamel baxadzayn')
# else : print('Baxadzayn')

#38 '''Alber jan es chishtem grel mi hat kstuges'''
# a = int(input('Nermuceq tiv-->'))
# if (a <= 10 and a>= 3) :
#     if (a == 4):
#         print('Qarakusi')
#     else : print(f'{a} ankyun')
# else : print('tivy 3-10 mijakayqi mej che')

#39
# amis = input('Nermuceq amisy--> ')
# _31_amis = ['Hunvar','Mart','Mayis','Hulis','Ogostos','Hoktember','Dektember']
# if amis in _31_amis :
#     print('31 or')
# elif amis == 'Petrvar' :
#     print('28 kam 29 or')
# else : print('30 or')

#40
# Decibel = float(input('Громкость звука --> '))
# if Decibel == 40 :
#     print('Тихая комната')
# elif (Decibel > 40 and Decibel < 70):
#     print('Тихая комната и Будильник')
# elif Decibel == 70:
#     print('Будильник')
# elif (Decibel > 70 and Decibel < 106):
#     print('Будильник и Газовая газонокосилка')
# elif Decibel == 106:
#     print('Газовая газонокосилка')
# elif (Decibel > 106 and Decibel < 130):
#     print('Газовая газонокосилка и Отбойный молоток')
# elif Decibel == 130 :
#     print('Отбойный молоток')
# else :
#     print('Отбойный молоток и больше')

#41
# a = int(input('Arajin koxmi erkarutyun --> '))
# b = int(input('Erkrod koxmi erkarutyun --> '))
# c = int(input('Errord koxmi erkarutyun --> '))
# if (a == b and a == c):
#     print('Havasarakoxm errankyun')
# elif((a == b or a == c) or b == c):
#     print('errankyan 2 koxmery havasar en ')
# else : print('Errankyun vorri vochmi koxm havasar che')

#42 '''Albert jan esel mi hat stugi chishtem grel te che '''
# nota = input('Nota --> ')
# x = float(input('Octava-->'))
# if (nota == 'C' and ( x > 0 and x <= 5)):
#     print(261.63 * x)
# elif nota == 'D' and (x > 0 and x <=5):
#     print(293.66 * x)
# elif nota == 'E' and (x > 0 and x <=5):
#     print(329.63 * x)
# elif nota == 'F' and (x > 0 and x <=5):
#     print(349.23 * x)
# elif nota == 'G' and (x > 0 and x <=5):
#     print(392 * x)
# elif nota == 'A' and (x > 0 and x <=5):
#     print(440 * x)
# elif nota == 'B' and (x > 0 and x <=5):
#     print(493.88 * x)
# else : 
#     print('Sxal nermucvac octava kam nota')

#44
# gumar = int(input('poxy --> '))
# if gumar == 1 :
#     print('Jorge Vashington')
# elif gumar == 2 :
#     print('Tomas Jefferson')
# elif gumar == 5 :
#     print('Abraham Linkoln')
# elif gumar == 10 :
#     print('Alexandr Gamilton')
# elif gumar == 20 :
#     print('Endryu Jekson')
# elif gumar == 50 :
#     print('Uliss Grant')
# elif gumar == 100 :
#     print('Benjamin Franklin')
# else : 
#     print('Nshvac pox chka ')

#45
# ory = input('Ory --> ')
# amis = input('Amis --> ')
# if (amis == 'Hunvar' and ory == '1'):
#     print('Nor tari')
# elif (amis == 'Hulis' and ory == '1'):
#     print('Canadai or')
# elif (amis == 'Dektember' and ory == '25'):
#     print('Surb Cnund')
# else : print('Ayd ory Canadayum ton che')

#46
# let = input('Tarry --> ')
# tiv = int(input('Nermuceq tiv 1-8 mijakayqum --> '))
# severov_sksvox = ['a','c','e','g']
# spitaknerov_sksvox  = ['b','d','f','h']
# if (let in severov_sksvox and tiv % 2 == 0): #tveri hamar karam avelacnem stex payman vor stugi 8i meja te che prosto inputi mej grelem vor 1-8 mijakayqum
#     print('Spitak')
# elif(let in severov_sksvox and tiv % 2 != 0):
#     print('Sev')
# elif(let in spitaknerov_sksvox and tiv % 2 == 0):
#     print('Sev')
# elif (let in spitaknerov_sksvox and tiv % 2 != 0):
#     print('Spitak')
# else :
#     print('Sxal tiv kam tarr')

#47
# amis = input('Amis --> ')
# ory = int(input('Ory --> '))
# Garun = ['April','Mayis','Hunis']
# Amar = ['Hulis','Ogostos','September']
# Ashun = ['Hoktember','Noyember','Dektember']
# Dzmer = ['Hunvar','Petrvar','Mart']
# if amis in Garun:
#     if amis == 'Hunis' and ory >= 21:
#         print('Amar')
#     else: print('Garun')
# elif amis in Amar:
#     if amis == 'September' and ory >= 22:
#         print('Ashun')
#     else : print('Amar')
# elif amis in Ashun:
#     if amis == 'Dektember' and ory >= 21:
#         print('Dzmer')
#     else : print('Ashun')
# elif amis in Dzmer:
#     if amis == 'Mart' and ory >= 20:
#         print('Garun')
#     else : print('Dzmer')

#48'''Es xndiry erkara stacvel 47 toxa grac grqum im mot 49
# amis = input('Amis --> ')
# ory = int(input('Ory --> '))
# if amis == 'Dektember':
#     if ory >=22 :
#         print('Aycexjur')
#     else : print('Axexnavor')
# elif amis == 'Hunvar':
#     if ory >= 20 :
#         print('Jrhos')
#     else : print('Aycexjur')
# elif amis == 'Petrvar':
#     if ory >= 19:
#         print('Dzuk')
#     else : print('Jrhos')
# elif amis == 'Mart':
#     if ory >= 21:
#         print('Xoy')
#     else : print('Dzuk')
# elif amis == 'April':
#     if ory >= 20:
#         print('Cul')
#     else: print('Xoy')
# elif amis == 'Mayis':
#     if ory >= 21:
#         print('Zuyg')
#     else : print('Cul')
# elif amis == 'Hunis':
#     if ory >= 21:
#         print('Xecgetin')
#     else : print('Zuyg')
# elif amis == 'Hulis':
#     if ory >= 23:
#         print('Aryuc')
#     else : print('Xecgetin')
# elif amis == 'Ogostos':
#     if ory >= 23:
#         print('Kuys')
#     else : print('Aryuc')
# elif amis == 'September':
#     if ory >=23 :
#         print('Ksherq')
#     else: print('Kuys')
# elif amis == 'Hoktember':
#     if ory >=23:
#         print('Karich')
#     else : print('Ksherq')
# elif amis == 'Noyember':
#     if ory < 22:
#         print('Karich')
#     else : print('Aycexjyur')

#49
# tiv = int(input('Nermuceq cnvelu taretivy-->'))
# if tiv % 12 == 2000 % 12 :
#     print('Drakon')
# elif tiv % 12 == 2001 % 12 :
#     print('Odz')   
# elif tiv % 12 == 2002 % 12 :
#     print('Dzi') 
# elif tiv % 12 == 2003 % 12:
#     print('Ayc') 
# elif tiv % 12 == 2004 % 12:
#     print('Kapik') 
# elif tiv % 12 == 2005 % 12:
#     print('Aqlor') 
# elif tiv % 12 == 2006 % 12:
#     print('Shun') 
# elif tiv % 12 == 2007 % 12:
#     print('Xoz') 
# elif tiv % 12 == 2008 % 12:
#     print('Kris') 
# elif tiv % 12 == 2009 % 12:
#     print('Cul') 
# elif tiv % 12 == 2010 % 12:
#     print('Aryuc') 
# elif tiv % 12 == 2011 % 12:
#     print('Naptastak') 

#50
# tiv = float(input('Nermuceq Magnitudan --> '))
# if tiv < 2 :
#     print('Minimal')
# elif tiv >= 2 and tiv < 3:
#     print('Shat tuyl')
# elif tiv >= 3 and tiv < 4:
#     print('Tuyl')
# elif tiv >= 4 and tiv < 5:
#     print('Mijankyal')
# elif tiv >= 5 and tiv < 6:
#     print('Chapavor')
# elif tiv >= 6 and tiv < 7:
#     print('Ujex')
# elif tiv >= 7 and tiv <8:
#     print('Shat ujex ')
# elif tiv >= 8 and tiv < 10:
#     print('Ahavor')
# elif tiv >= 10 :
#     print('Koracanarar')

#51
# import math
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# disc = b ** 2 - 4 * a * c
# if disc == 0 :
#     x1 = -b / (2 * a)
#     print(f' 1 armat \n {x1}')
# elif disc < 0 :
#     print(' 0 \n Armat chuni')
# else :
#     x1 = -b + math.sqrt(disc / (2 * a))
#     x2 = -b - math.sqrt(disc / (2 * a))
#     print(f' 2 armat\n arajin army --> {x1}\n erkord armaty --> {x2}')

#52
# taranshan = input('Tarain nshany --> ')
# if 'A' in taranshan:
#     if '-' in taranshan:
#         print(4 - 0.3)
#     else: print(4)
# elif 'B' in taranshan:
#     if '-' in taranshan:
#         print(3.3)
#     elif '+' in taranshan:
#         print(3.3)
#     else : print(3)
# elif 'C' in taranshan:
#     if '-' in taranshan:
#         print(2.3)
#     elif '+' in taranshan:
#         print(2.3)
#     else : print(3)
# elif 'D' in taranshan:
#     if '+' in taranshan:
#         print(1.3)
#     else : print(1)
# elif 'F' in taranshan:
#     print(0)

#53
# tvanshan = float(input('Nermuceq tvanshany -->'))
# if tvanshan > 4 :
#     print('A+')
# elif tvanshan <= 4 and tvanshan > 3.7:
#     print('A')
# elif tvanshan <= 3.7 and tvanshan > 3.3:
#     print('A-')
# elif tvanshan <= 3.3 and tvanshan > 3:
#     print('B+')
# elif tvanshan <= 3 and tvanshan >2.7:
#     print('B')
# elif tvanshan <= 2.7 and tvanshan > 2.3:
#     print('B-')
# elif tvanshan <= 2.3 and tvanshan > 2:
#     print('C+')
# elif tvanshan <= 2 and tvanshan > 1.7:
#     print('C')
# elif tvanshan <=1.7 and tvanshan >1.3:
#     print('C-')
# elif tvanshan <= 1.3 and tvanshan > 1:
#     print('D+')
# elif tvanshan <= 1 and tvanshan > 0:
#     print('D')
# else : print('F')

#54
# rating = float(input('Nermuceq ashxatoxi reytingy--> '))
# if rating == 0 :
#     print('"Cacr makardak"\n0 gumar ashxatavardzi barcracman hamar')
# elif rating ==0.4:
#     print(2400 * rating)
#     print('Bavarar makardak')
# elif rating >= 0.6:
#     print(rating * 2400)
#     print('Bardzr Makaradak')
# else : print('Sxal nshvac makardak')

#55
# erkarutyun = int(input('Aliqi erakrutyun--> '))
# if erkarutyun >= 380 and erkarutyun < 450:
#     print('Manushakaguyn')
# elif erkarutyun >= 450 and erkarutyun < 495:
#     print('Kapuyt')
# elif erkarutyun >= 495 and erkarutyun < 570:
#     print('Kanach')
# elif erkarutyun >= 570 and erkarutyun < 590:
#     print('Dexin')
# elif erkarutyun >= 590 and erkarutyun < 620:
#     print('Gazaraguyn')
# elif erkarutyun >= 620 and erkarutyun <= 750:
#     print('Karmir')
# else : print('Error')

#56
# a = float(input('Hachaxakanutyuny --> '))
# if a < 3 * (10 ** 9) : 
#     print('Radioaliq')
# elif a >= 3 * (10 ** 9) and a < 3 * (10 ** 12):
#     print('Mikroaliq')
# elif a >= 3 * (10 ** 12) and a < 4.3 * (10 ** 14):
#     print('Infrakarmir Charagayt')
# elif a >= 4.3 * (10 ** 14) and a < 7.5 * (10 ** 14):
#     print('Tesaneli charagayt')
# elif a >= 7.5 * (10 ** 14) and a < 3 * (10 ** 17):
#     print('Ultramanushakaguyn charagayt')
# elif a >= 3 * (10 ** 17) and a < 3 * (10 ** 19):
#     print('Rengenain charagayt')
# else: print('Gamma charagayt')

#57
# ropener = float(input('Ropenery xosalu--> '))
# smsnery = float(input('SMS nery --> '))
# amis = 15
# if ropener // 50 != 0 :
#     amis = amis + (((ropener//50) * 50)-ropener) * 0.25
# if smsnery // 50 != 0 :
#     amis = amis + (((smsnery//50) * 50)-smsnery) * 0.15
# nalog = amis * 5 / 100
# print(f' Amsakan vchary = 15.0$ \n Lracucich ropei gumary = 0.25$ \n Lracucich SMS i gumary = 0.15$ \n Nalog ={round(nalog,2)}$ \n Call centre i gumar = 0.44$ \n Yndhanur gumar ={round(amis,2)}$ ')

#59
# ory = int(input('Amsva or -->'))
# amis = input('amis --> ')
# tari = int(input('Tari -->'))
# _31_amis = ['Hunvar','Mart','Mayis','Hulis','Ogostos','Hoktember','Dektember']
# _30_amis = ['April','Hunis','September','Noyember']
# if ory < 30:
    
#     if amis == 'Petrvar' and ory == 28:
#         amis = 'Mart'
#         ory = 1
#         print(f'{amis} {ory} {tari}')
#     else:
#         ory = ory + 1
#         print(f'{amis} {ory} {tari}')
# if ory == 30 :
#     if amis == 'April':
#         ory = 1
#         amis = 'Mayis'
#         print(f'{amis} {ory} {tari}')
#     elif amis == 'Hunis':
#         ory = 1
#         amis = 'Hulis'
#         print(f'{amis} {ory} {tari}')
#     elif amis == 'September':
#         ory = 1
#         amis = 'Hoktember'
#         print(f'{amis} {ory} {tari}')
#     elif amis == 'Noyember':
#         ory = 1
#         amis = 'Dektember'
#         print(f'{amis} {ory} {tari}')
#     else : 
#         ory += 1
#         print(f'{amis} {ory} {tari}')
         
# if ory == 31:
#     ory = 1
#     if amis == 'Hunvar':
#         amis =='Petrvar' 
#         print(f'{amis} {ory} {tari}')
#     elif amis == 'Mart':
#         amis == 'April'
#         print(f'{amis} {ory} {tari}')
#     elif amis == 'Mayis':
#         amis = 'Hunis'
#         print(f'{amis} {ory} {tari}')
#     elif amis == 'Hulis':
#         amis = 'Ogostos'
#         print(f'{amis} {ory} {tari}')
#     elif amis =='Ogostos':
#         amis = 'September'
#         print(f'{amis} {ory} {tari}')
#     elif amis == 'Hoktember':
#         amis = 'Noyember'
#         print(f'{amis} {ory} {tari}')
#     elif amis == 'Dektember':
#         tari += 1
#         amis = 'Hunvar'
#         print(f'{amis} {ory} {tari}')

#60
# import math
# tari = int(input('Tari --> '))
# day_of_the_week = (tari + math.floor((tari - 1)/4) - math.floor((tari - 1)/ 100) + math.floor((tari - 1)/400)) % 7 
# print(day_of_the_week)
# if day_of_the_week == 6 :
#     print('Saturday')
# elif day_of_the_week == 5:
#     print('Friday')
# elif day_of_the_week == 4:
#     print('Thursday')
# elif day_of_the_week == 3:
#     print('Wednesday')
# elif day_of_the_week == 2:
#     print('Tuesday')
# elif day_of_the_week == 1:
#     print('Monday')
# else :
#     print('Sunday')

#61
# import math
# pethamaranish = input('Pethamaranish --> ')
# print('Hin hamaranishi dzev --> "ABC123"\nNor hamaranishi dzev --> "1234ABC"')

# if pethamaranish[0].isalpha() :
#     if pethamaranish[1].isalpha():
#         if pethamaranish[2].isalpha():
#             if pethamaranish[3].isdigit():
#                 if pethamaranish[4].isdigit():
#                     if pethamaranish[5].isdigit():
#                             print('Hin pethamaranish')
#     else :
#         print('Sxal pethamaranish')
# if pethamaranish[0].isdigit() :
#     if pethamaranish[1].isdigit():
#         if pethamaranish[2].isdigit():
#             if pethamaranish[3].isdigit():
#                 if pethamaranish[4].isalpha():
#                     if pethamaranish[5].isalpha():
#                         if pethamaranish[6].isalpha():
#                             print('Nor pethamaranish')
#     else :
#         print('Sxal pethamaranish')

#62
# import random
# print('Xaxadruyqi tesakner`\nmek tiv 0-38 mijakayqum ev 00\nKarmir kam Sev\nKent kam zuyg(0 ev 00n chen hamarvum zuyg kam kent)\n1-18 mijakayq kam 19-36')
# stavka = input('Dzer xaxadruyqy -->')
# karmir = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30,32, 34 ,36)
# sever = (2,4,6,8,10,11,13,15,17,20,22,24,26,28,39,31,33,35,37,38)
# bolory = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,36,'0','00')
# a = random.choice(bolory)
# if a == '0':
#     print('Haxtac tiv --> 0\n Haxtelu tiv --> 0')
# elif a == '00':
#     print('Haxtac tiv --> 00\n Haxtelu tiv --> 00')
# elif type(a) == type(1):
#     if a > 0 and a<=18:
#         if a in karmir:
#             if a % 2 == 0:
#                 print(f'yngac tiv --> {a}\nhaxtac tiv --> {a}\nHaxtac stavka --> Karmir\nHaxtac stavka -->Zuyg\nHaxtac stavka -->1-18 mijakayq')
#             elif a % 2 != 0 :
#                 print(f'yngac tiv --> {a}\nhaxtac tiv --> {a}\nHaxtac stavka --> Karmir\nHaxtac stavka -->Kent\nHaxtac stavka -->1-18 mijakayq')
#         if a in sever:  
#             if a % 2 == 0:
#                 print(f'yngac tiv --> {a}\nhaxtac tiv --> {a}\nHaxtac stavka --> Sev\nHaxtac stavka -->Zuyg\nHaxtac stavka -->1-18 mijakayq')
#             elif a % 2 != 0 :
#                 print(f'yngac tiv --> {a}\nhaxtac tiv --> {a}\nHaxtac stavka --> Sev\nHaxtac stavka -->Kent\nHaxtac stavka -->1-18 mijakayq')
#     if a > 18 and a <= 36:
#         if a in karmir:
#             if a % 2 == 0:
#                 print(f'yngac tiv --> {a}\nhaxtac tiv --> {a}\nHaxtac stavka --> Karmir\nHaxtac stavka -->Zuyg\nHaxtac stavka -->19-36 mijakayq')
#             elif a % 2 != 0 :
#                 print(f'yngac tiv --> {a}\nhaxtac tiv --> {a}\nHaxtac stavka --> Karmir\nHaxtac stavka -->Kent\nHaxtac stavka -->19-36 mijakayq')
#         if a in sever:  
#             if a % 2 == 0:
#                 print(f'yngac tiv --> {a}\nhaxtac tiv --> {a}\nHaxtac stavka --> Sev\nHaxtac stavka -->Zuyg\nHaxtac stavka -->19-36 mijakayq')
#             elif a % 2 != 0 :
#                 print(f'yngac tiv --> {a}\nhaxtac tiv --> {a}\nHaxtac stavka --> Sev\nHaxtac stavka -->Kent\nHaxtac stavka -->19-36 mijakayq')


        

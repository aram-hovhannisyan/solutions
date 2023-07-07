#16

# import math 

# r = int(input('sharavixy --> '))
# area = 2 * math.pi * r
# volume = 4 /3 * math.pi * r
# print(f'area = {round(area,2)} \n volume = {round(volume , 2)}')

#17

# m = float(input('massan inchqana --> '))
# T = float(input('jermastichany inchqana --> '))
# C = m * 4.186 
# q = C * m * T
# Print(f'Energian havasar e --> {q} Joul')
# q_kofe = (50 * 4.186) * 50 * T

#18

# import math 
# r = int(input('sharavixy --> '))
# h = int(input('barcrutyuny --> '))
# makeres = 2 * math.pi * r
# volume = makeres * h
# print(f'{round(volume , 1)}')

#19
# import math
# h = int(input('barcrutyuny --> '))
# a =  math.sqrt(2 * 9.8 * h)
# print(f'aragutyuny = {a}')

# #20 
# P = int(input('chnshum-->'))
# V = int(input('caval-->'))
# T = int(input('jermastichan-->'))
# n = P * V / 8.314 * T
# print(f'qanak = {n}')

#21
# b = int(input('koxmi erkarutyun--> '))
# h = int(input('koxmi bardzrutyun--> '))
# s = b * h
# print(s)

#22
# import math

# s1 = int(input('arajin koxmi erkrutyun'))
# s2 = int(input('erkrord koxmi erkrutyun'))
# s3 = int(input('errord koxmi erkrutyun'))
# s = (s1 + s2 + s3) / 2
# area = math.sqrt(s * (s-s1) * (s-s2) * (s - s3))
# print(area) 

#23
# import math
# s = int(input('koxmi erkarutyun --> '))
# n = int(input('koxmeri qanak --> '))
# area = n * (s ** 2)/ 4 * math.tan(math.pi / n)
# print(area)

#24

# orer = int(input('orery -> '))
# jamery = int(input('jamery -> '))
# ropener = int(input('ropenery -> '))
# vayrkyanner = int(input('vayrkyanner -> '))
# vayrkyannery_yndhanur = (orer * 24 * 60 * 60) + (jamery * 60 * 60) + (ropener * 60) + vayrkyanner
# print(vayrkyannery_yndhanur)

#26
# import time 
# b = time.asctime()
# print(b)

#28

# hasak = int(input('dzer hasaky --> '))
# qashy = int(input('dzer qashy --> '))
# BMI = qashy / hasak ** 2 
# print(BMI)

#29

# T = float(input('Jermastichany --> '))
# V = float(input('Aragutyuny --> '))
# print(V ** 0.16)
# WCI = 13.12 + 0.6215 * T - 11.37 * (V ** 0.16) + 0.3965 * (V ** 0.16)
# print(round(WCI,0))

#30

# celsus = float(input('Qani celsus = '))
# far = celsus * 1.8 + 32 
# print(f'{celsus} esqan celsus havasar e {far} farenhayti')

#31
# import math
# pascal = int(input('pascalner--> '))
# PSI = pascal * 0.1450377377
# MILIMETR = pascal * 7.50062
# ATM = pascal * 0.00986923 
# print(f' kilopascal = {pascal}\n PSI = {PSI} \n MILIMETR = {MILIMETR} \n ATM = {ATM}')

#32

# a = int(input('Qaranish tiv nermuceq --> '))
# b = (a//1000)%10 + (a//100)%10 + (a//10)%10 + a%10
# print(b)
# print(f'{(a//1000)%10} + {(a//100)%10} + {(a//10)%10} + {a % 10} = {b}')

#33

# import math

# a = int(input('arajin tiv--> '))
# b = int(input('erkrord tiv--> '))
# c = int(input('errord tiv--> '))
# minimum = min(a,b,c)
# maximum = max(a,b,c)
# mejtex = (a+b+c)-(maximum+minimum)
# print(f'{minimum}\t{mejtex}\t{maximum}')

#34
# aracner = int(input('eregva arac Haceri qanak --> '))
# eregva_arac = aracner * 3.49 * 60 / 100
# zexchvac_gin = 3.49 * 60 / 100
# print(f' Irakan arjeqy \t\t 3.49$ \n Erekva Zexchvac giny \t {round(zexchvac_gin,2)}$ \n Ir tvac gumary \t {round(eregva_arac,2)}$')

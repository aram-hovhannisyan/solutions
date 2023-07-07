#1
# print(f' Karen Melkonyan Armeni \n karenmelkonyan199@gmail.com')

#2
# name = input('What is your name? ')
# print(f'Hello {name}')

#3
# a = float(input('Qani metre taracqi erkarutyuny '))
# b = float(input('Qani metre taracqi laynutyuny '))
# S = a * b
# print(f'Taracqi makeresy havasar e {S} metr qarakusi ')

#4
# a = float(input('Qani fute taracqi erkarutyuny '))
# b = float(input('Qani fute taracqi laynutyuny '))
# a = a / 43560
# b = b / 43560
# S = a * b 
# print(f'Taracqi makeresy akrerov havasar e {S}')

#5
# a = float(input('Qani shish 1L ic cacr-->'))
# b = float(input('Qani shish 1L ic bardzr-->'))
# a = a * 0.10 
# b = b * 0.25
# c = a + b
# print(f'Petqe vchari  {round(c,2)}$')

#6
# zakaz = float(input('Zakazi gumary--> '))
# chayevoy = zakaz * 18 / 100 
# Nalog = zakaz * 20 / 100
# Hashiv = zakaz + chayevoy
# print(f'Chayevoy@ havasara = {chayevoy} \n Nalogy = {Nalog} \n Hashiv = {Hashiv}')

#7
# n = int(input('nermuceq 1 ev barcr bnakan tiv --> '))
# SUM = n * (n + 1) / 2
# print(f'{n} i mijev gtnvox tveri gumary havasar e {round(SUM)}')

#8
# suvenir = int(input('qani hat suvenir eq cankanum gnel -->'))
# hushanver = int(input('qani hat hushanver eq cankanum gnel -->'))
# suvenir_gram = suvenir * 75
# hushanver_gram = hushanver * 112
# print(f'yndhanur arac apranqi qashy havasar e  {suvenir_gram+hushanver_gram}')

#9
# gumar = int(input('mutqagreq gumary -->'))
# _1_tari = gumar + gumar * 4 / 100
# _2_tari = _1_tari + _1_tari * 4 / 100
# _3_tari = _2_tari + _2_tari * 4 / 100
# print(f' 1 tari = {round(_1_tari,2)} \n 2 tari = {round(_2_tari,2)} \n 3 tari = {round(_3_tari,2)}')

#10
#  '''Albert jan math i het kapvaca es iport math anum '''
# import math
# a = int(input('nermuceq a tivy --> '))
# b = int(input('nermuceq b tivy --> '))
# sum = a + b
# hanum = a - b
# average = a * b
# bajanum = a / b 
# mnacord = a % b 
# logaritm = math.log10(a)
# astichan = a ** b
# print(f' gumary = {sum} \n hanumy = {hanum} \n bazmapatkum = {average} \n bajanum = {bajanum} \n mnacord = {mnacord} \n logaritm 10 himqov = {logaritm} \n a-i b astichany = {astichan}')

#11
# a = int(input('How much MGP-->'))
# b = 235.214583 / a
# print(f' MGP = {a} \n L/100 = {b}')

#12
# import math


# a_1 = float(input('Araji keti x kordinat--> '))
# a_2 = float(input('Araji keti y kordinat--> '))
# b_1 = float(input('Erkrord keti x kordinat--> '))
# b_2 = float(input('Erkrord keti y kordinat--> '))
# a_1_radian = math.radians(a_1)
# a_2_radian = math.radians(a_2)
# b_1_radian = math.radians(b_1)
# b_2_radian = math.radians(a_2)
# heravorutyun = 6371.01 * math.acos(math.sin(a_1_radian) * math.sin(b_1_radian)+ math.cos(a_1_radian) * math.cos(b_1_radian) *math.cos(a_2 - b_2))
# print(f'heravorutyuny ayd keteri mijev havasar e __> {heravorutyun}')

#13

# gumary = float(input('Mutqagreq gumary -->'))
# _25_centanoc = gumary // 25 
# _10_centanoc = (gumary - _25_centanoc * 25 ) // 10
# _5_centanoc = (gumary - _25_centanoc * 25 - _10_centanoc * 10) // 5
# _1_centanoc = (gumary - _25_centanoc * 25 - _10_centanoc * 10 - _5_centanoc * 5) // 1
# print(f' 25 kopekanoc = {round(_25_centanoc)} \n 10 kopekanoc = {round(_10_centanoc)} \n 5 kopekanoc = {round(_5_centanoc)} \n 1 kopekanoc = {round(_1_centanoc)}')

#14
# futter = float(input('qani fut -->'))
# dyum = float(input('qani dyum -->'))
# futter_dyum = futter * 12
# hasaky = (dyum + futter_dyum) * 2.54
# print(f'hasaky havasar e {hasaky}')

#15

# fut = float(input('vorqan fut eq cankanum hashvarkel-->'))
# dyum = 12 * fut
# yard = dyum * 0.0278
# mil = yard * 0.000568
# print(f' dyumery = {dyum} \n yard = {yard} \n mil = {mil}')
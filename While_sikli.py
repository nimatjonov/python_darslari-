# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 21:33:00 2024

@author: user
"""

#son = 1 
#while son <=5:
#    print(son, end=' ')
 #   son = son + 1
    
    
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)


import random

secret_number = random.randint(1, 10)
guess = None
while guess != secret_number:
    guess = int(input("1 dan 10 gacha bo'lgan sonni toping: "))
    if guess < secret_number:
        print("Kiritgan soningiz kichik.")
    elif guess > secret_number:
        print("Kiritgan soningiz katta.")
    else:
        print("To'g'ri topdingiz!")
        
print("Do'stlaringiz yoshini saqlaymiz.")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingiz ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False

for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")

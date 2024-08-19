# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:53:18 2024

@author: user
"""

def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")
    
    
def to_uppercase(s):
    return s.upper()

# Sinash
print(to_uppercase("hello world"))  # "HELLO WORLD"
print(to_uppercase("Python"))       # "PYTHON"



def yosh_hisobla(tugilgan_yil, joriy_yil=2024):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
tyil = int(input("Tug'ilgan yilingizni kiriting: "))
yosh_hisobla(tyil)



# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
def juftmi(son):
    """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
    if son%2:
        print(f"{son} toq son")
    else:
        print(f"{son} juft son")

juftmi(20)
juftmi(123)


# Foydalanuvchidan son qabul qilib, sonni 2, 3, 4 va 5 ga qoldiqsiz bo'linishini tekshiruvchi 
# Natijalarni konsolga chiqaring ("15 soni 3 ga qoldiqsiz bo'linadi" ko'rinishida)
def bolinish_alomatlari(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(20)
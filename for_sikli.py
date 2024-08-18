# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 03:11:49 2024

@author: user
"""

friends=['sardor ', 'ali', 'sanjar ', 'jamol']
for friend in friends :
    print(f"Assalomu alaykum {friend.capitalize()}")
    



dostlar = [] # bo'sh ro'yxat

print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)

for i in range(1, 6):
    print(i, "ning kvadrati:", i**2)
 

for i in range(1, 11):
    if i % 2 == 0:
        print(i, "juft son")

sonlar = [2, 4, 6, 8, 10]
yigindi = 0
for son in sonlar:
    yigindi += son
print("Yig'indi:", yigindi)

n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))



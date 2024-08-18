# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:08:08 2024

@author: user
"""
avtolar =[ 'audi', 'mers', 'bmw','toyota' ,'tesla']
for avto in avtolar:
    if avto =='bmw':
        print(avto.upper())
    else:
        print(avto.title())
        
        
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} juft son")
    else:
        print(f"{i} toq son")


sonlar = [10, -5, 7, -2, 0, 3, -1]

for son in sonlar:
    if son > 0:
        print(f"{son} musbat son")
    elif son < 0:
        print(f"{son} manfiy son")
    else:
        print(f"{son} nol")

foydalanuvchilar = ["Ali", "Olmos", "Shirin", "Olim", "Bekzod"]
for ism in foydalanuvchilar:
    if len(ism)>5:
        print(f"{ism} - uzun")
    else:
        print(f"{ism} - qisqa  yoki teng ")


parollar = ["123456", "parol123", "qwerty", "Uzbek!123"]

for parol in parollar:
    if len(parol) >= 8 and not parol.isdigit():
        print(f"{parol} - xavfsiz.")
    else:
        print(f"{parol} - xavfsiz emas.")
 
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
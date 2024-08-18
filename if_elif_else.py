# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:31:27 2024

@author: user
"""

yosh = int(input('Yoshingiz nechida? '))
if yosh<=4:
    print('Sizga kirish bepul.')
elif yosh<=12:
    print('Sizga kirish 5000 so\'m')
else:
    print('Sizga kirish 10000 so\'m')


soz = "Salom"

if len(soz) > 10:
    print("Juda uzun so'z")
elif len(soz) >= 5:
    print("O'rtacha uzunlikdagi so'z")
else:
    print("Qisqa so'z")

    
 #foydalanuvchini bahosini baholash   
    
bahosi = int(input("Iltimos balingizni kiriting  kirting "))

if bahosi >= 90:
    print("Alo")
elif bahosi >=80:
    print("Yaxshi")
elif bahosi >=70 :
    print("Qoniqarli")
elif bahosi >= 55:
    print("Qoniqrsiz")
else : 
    print("Imtihondan o'tmadi")
    
#kun harorati 
harorat = int(input("Bugun harorat nechi"))

if  harorat > 30:
    print("Bugun havo issiq ")
elif harorat >= 20 :
    print("Bugun havo narmanli ")
elif harorat >=10 :
    print("Bugun havo salqin")
elif harorat >=0:
    print("Bugun havo sovuq ")
else:
    print("Bugun juda sovuq")
    
    





























    
    

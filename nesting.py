# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:11:40 2024

@author: user
"""

# for sikli yordami bitta ruyxat  yaratib olamiz 
toyota =[]

for  n in range (10):
    new_car = {
        'model': 'Prado',
        'color': None ,
        'year': 2019,
        'price':None,
        'km':0,
        'transmission':'avto'
        }
    toyota.append(new_car)
    
    
    
# Tepada  yaratgan ro'yxatda color ga qiymat bermadik shunga hozir qiymay beramiz 

for Prado in toyota[:3]:
    Prado['color']='black'
    
# keyin 3 taga ham rang  beramiz
for Prado in toyota [3:6]:
    Prado['color']='write'


for Prado in toyota[6:10]:
    Prado['color']='yellow'


for Prado in toyota:
    if Prado['transmission']=='avto':
        Prado['price']=40000
    else:
        Prado['price']=35000


print(toyota)


dasturchilar = {
    'ali':{'familiya':'valiyev',
           'tyil':2002,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2004,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':2003,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }

for ism, info in dasturchilar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())
        
        
countries= {
    "o'zbekiston":{'capital':"toshkent",
                   'field':448978,
                   'population':33_000_000,
                   'monetary unit':"so'm"
                   },
    "rossiya":{'capital':"moskva",
                   'field':17_098_246,
                   'population':144_000_000,
                   'monetary unit':"rubl"
                   },
    "aqsh":{'capital':"vashington",
                   'field':9_631_418,
                   'population':327_000_000,
                   'monetary unit':"dollar"},
    "malayziya":{'capital':"kuala-lumpur",
                   'field':329750,
                   'population':25_000_000,
                   'monetary unit':"rinngit"}
    }

for country, info in countries.items():
    if country.lower()=='aqsh':
        country = country.upper()
    else:
        country = country.capitalize()
    print(f"\n{country}ning poytaxti {info['capital'].title()}"
          f"\nHududi: {info['field']} kv.km"
          f"\nAholisi: {info['population']}"
          f"\nPul birligi: {info['monetary unit']}")
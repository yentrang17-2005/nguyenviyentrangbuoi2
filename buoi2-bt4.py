# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:20:45 2024

@author: Admin
"""

a = float(input("Tổng số km (km>1):  "))
if a==1: 
   print("Tổng số tiền:",20000)
elif 1<a<4:
   print("Tổng số tiền:",20000 + (a-1)*13000)
elif 4<=a<9:
   print("Tổng số tiền:",3*130000 + (a-3)*12000)
elif 9<=a<=100:
   print("Tổng số tiền:",3*13000 + 5*12000 + (a-8)*10000)
else:
   print("Tổng số tiền:",(3*13000 + 5*12000 + (a-8)*10000)*(0.92))
  
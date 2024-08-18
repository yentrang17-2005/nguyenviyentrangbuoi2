# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:22:10 2024

@author: Admin
"""
a = float(input("Nhập giá trị của a:"))
b = float(input("Nhập giá trị của b:"))
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    if b != 0: 
        print("Phương trình vô nghiệm")
if a!= 0:
    x = -b/a
    print("Nghiệm phương trình là:",x)

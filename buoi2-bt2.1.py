# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:18:47 2024

@author: Admin
"""

print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
a = float(input("Nhập giá trị của a:"))
b = float(input("Nhập giá trị của b:"))
c = float(input("Nhập giá trị của c:"))
delta=float
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
                
    else:
        if c == 0:
            print("Phương trình có 1 nghiệm x=0")
        else:
            print("Phương trình có nghiệm x=",-c/b)
    
else:
    delta = b*b - 4*a*c
    if delta < 0:  
        print("Phương trình vô nghiệm") 
    elif delta == 0:
        print("Phương trình có nghiệm kép x1=x2=",-b/(2*a))      
    else:
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1=",-b-((delta)*1/2)/(2*a))
        print("x2=",-b+((delta)*1/2)/(2*a))  
                
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:50:21 2024

@author: Admin
"""
print("Có phải tam giác?")
a = float(input("Cạnh a (a !=0) ="))
b = float(input("Cạnh b (b !=0) ="))
c = float(input("Cạnh c (c !=0) ="))
if a+b>c and b+c>a and c+a>b:
    print("Đó là tam giác")
    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        print("Loại tam giác: Tam giác vuông")
    elif a==b and b==c and a==c:
        print("Loại tam giác: Tam giác đều")
    elif a==b or a==c or b==c:
        print("Loại tam giác: Tam giác cân")
    else:
        print("Loại tam giác: Tam giác thường")
else: 
    print("Đó không phải là tam giác")
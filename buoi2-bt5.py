# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:43:08 2024

@author: Admin
"""

import random
ban=input("Ban chon gi? (bua,keo,bao): ")
cpt= random.choice(["keo","bua","bao"])
print("Ban chon:",{ban})
print("May chon:",{cpt})
if cpt==ban:
    print("hoa")
elif ban=="keo" and cpt=="bua" or ban=="bua" and cpt=="bao" or ban=="bao" and cpt=="keo":
        print("Ban da thua")
else:    
        print("Ban da thang")
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 00:30:09 2019

@author: lisa_
"""

def AND(a, b): 
    if a == 1 and b == 1: 
        return True
    else: 
        return False

def OR(a, b): 
    if a == 1: 
        return True
    elif b == 1: 
        return True
    else: 
        return False

def NOT(a): 
    if(a == 0): 
        return 1
    elif(a == 1): 
        return 0
    
def NAND(a, b): 
    if a == 1 and b == 1: 
        return False
    else: 
        return True

def NOR(a, b): 
    if a == 0 and b == 0: 
        return True
    elif a == 0 and b == 1: 
        return False
    elif a == 1 and b == 0: 
        return False
    elif a == 1 and b == 1: 
        return False
    
def XOR(a, b): 
    if a != b: 
        return True
    else: 
        return False


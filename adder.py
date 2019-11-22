# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 00:30:09 2019

@author: lisa_
"""

def AND(a, b): 
    if a == 1 and b == 1: 
        return 1
    else: 
        return 0

def OR(a, b): 
    if a == 1: 
        return 1
    elif b == 1: 
        return 1
    else: 
        return 0

def NOT(a): 
    if a == 0: 
        return 1
    elif a == 1: 
        return 0
    
def NAND(a, b): 
    if a == 1 and b == 1: 
        return 0
    else: 
        return 1

def NOR(a, b): 
    if a == 0 and b == 0: 
        return 1
    elif a == 0 and b == 1: 
        return 0
    elif a == 1 and b == 0: 
        return 0
    elif a == 1 and b == 1: 
        return 0
    
def XOR(a, b): 
    if a != b: 
        return 1
    else: 
        return 0
    
def Adder(a, b):
    Result = ''
    Count0 = 0
    n = -1
    while n >= -(len(a)):
        S = XOR(int(a[n]), int(b[n]))
        C = OR(AND(S, Count0), AND(int(a[n]), int(b[n])))
        S = XOR(S, Count0) 
        Count0 = C
        Result += str(S)    
        n -= 1
    Result += str(Count0)
    Result = Result[::-1]
    print(Result)

Adder("1111", "1111")
    

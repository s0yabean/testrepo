#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:47:35 2017

@author: tonytonggg
"""
###############################################################
import time
#start_time = time.time()
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
###############################################################
        
# time for O(1)
#start_time = time.time() 
factorial(190)
#print ("My program took", time.time() - start_time, "to run")

def func1(n):
    return n

start_time = time.time() 
func1(300)
print ("My program took", time.time() - start_time, "to run")

###############################################################
# time for O(n)

def func2(n):
    for i in range(n):
        if (i % 10) == 0:
            print("dividable by 10")
    
#start_time = time.time() 
func2(29)
#print ("My program took", time.time() - start_time, "to run")

###############################################################
# time for O(n^2)

def func3(n):
    for i in range(n):
        if (i % 10) == 0:
            print(i)
       #     print("dividable by 10")
        for p in range(n):
            if (p % 5) == 0:
                print(p)
              #  print("dividable by 5")
    
start_time = time.time() 
func3(500)
print ("My program took", time.time() - start_time, "to run")

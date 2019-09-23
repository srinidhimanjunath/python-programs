# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:29:53 2019

@author: srini
"""

def search(arr,x):
    flag=0
    count=0
    for i in arr:
        count = count+1
        if(i == x):
            print("Yes the element is found")
            flag = 1
            break
    if(flag==0):
        print("The element is not found in the list")
    print("The number of iterations required is : ",count)
element = []    
for i in range(1,1001):
    element.append(i)
n=int(input("Enter the NUmber that u want to search in the array"))
search(element,n)

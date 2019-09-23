# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:15:08 2019

@author: srini
"""

def bubble(arr):
    n=len(arr)
    for i in range (n):
        for j in range (n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
arr=[4,6,2,3,1]
bubble(arr)
print(arr)
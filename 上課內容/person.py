#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 19:22:50 2020

@author: roberthsu2003
"""
#module內的function
def sayHello():
    print("sayHello!")
    
#module內的類別
class Person:
    #建立自訂的初始化
    def __init__(self,name):
        print("建立了一個實體")
        #建立一個實體的屬性
        self.name = name;
    
    #實體方法
    def printName(self):
        print('我的名字是',self.name)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:13:31 2021

@author: jjberg
"""

def ask_and_strip():
    setning = input('Skriv en setning:\n')
    stripped = setning.strip('!:-,.')
    return stripped

if __name__ == '__main__':
    print('Dette er et nytt script')
    print(ask_and_strip())
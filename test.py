#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:13:31 2021

@author: jjberg
"""

setning = input('Skriv en setning:\n')
stripped = setning.strip(',.:-!')

if __name__ == '__main__':
    print('Dette er et nytt script')
    print(stripped)
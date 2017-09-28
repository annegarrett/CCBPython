# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:14:12 2017

@author: Anne
"""
def cipherfunc(myparam):
# Take each letter from user input and in each case:
    
    upper = myparam.upper()
        # - Convert to upper case
        
    alnum = [i for i in upper if i.isalnum() == True]
        # - Ignore any other (non-alpha) characters
     
    cipher=""
    
    for i in alnum:
        cipher+=str(i)
    # - In each case, add result to a string variable  
    
    # - Change numbers to words
    
    print(cipher)
    # print out the new string
    
    
    


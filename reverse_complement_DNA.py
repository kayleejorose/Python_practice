# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 19:24:53 2022

@author: kayle
"""

#This script create the reverse complement of a strand of DNA 

#Take DNA sequence as input 
DNA_seq = input("Enter the DNA sequence: ")

#reverse the sequence using slicing
#[start:stop:step]
#omitting start and stop since we want the entire string
#step to the left by 1 -> -1 
#We also start from the left
#so we iterate over the entire string from the left, going character by character
reverse_DNA = DNA_seq[::-1]

#now we complement the reverse DNA seq
old_chars = "ACGT" #characters to replace
replace_chars = "TGCA" #with these new characters--the respective complements 
reverse_complement = reverse_DNA.maketrans(old_chars,replace_chars) #maps each of the previous characters to the new chars
print("\n")
print(reverse_DNA.translate(reverse_complement))#translates into readable format 


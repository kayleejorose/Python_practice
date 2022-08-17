# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 19:19:46 2022

@author: kayle
"""
#This script transcribes a DNA sequence into RNA sequence by changing T to U 

#take DNA seq as input
DNA_seq = input("Enter the DNA sequence: ")
RNA_seq = DNA_seq.replace('T', 'U') #replace instances of T with U 

print("                                                          ")

print(RNA_seq)
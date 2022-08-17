# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 18:35:16 2022

@author: kayle
"""

#This script counts the number of each nucleotide in a DNA sequence 

#enter string of nucleotides
DNA_seq = input("Enter the DNA sequence: ")

#solved using a dictionary method
nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for nucleotide in DNA_seq:
    nucleotide_counts[nucleotide] = nucleotide_counts[nucleotide] + 1
    
print(nucleotide_counts['A'], nucleotide_counts['C'], nucleotide_counts['G'], nucleotide_counts['T'])

#this iterates one time instead of four or more, like previous problems 
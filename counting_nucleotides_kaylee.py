# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 15:29:22 2022

@author: kayle
"""

#enter string of nucleotides
DNA_seq = input("Enter the DNA sequence: ")
#checking if DNA seq. less than 1000 nucleotides 
if len(DNA_seq) >= 1000:
    print("Error: sequence must be less than 1000 nucleotides")
    raise SystemExit(0)
#defining counters for each nucleotide
a_ctr = 0
t_ctr = 0
c_ctr = 0
g_ctr = 0

#loop over seq length
for nucleotide in DNA_seq:
    if nucleotide == 'A': #counting instances of A
        a_ctr += 1
    elif nucleotide == 'T': #counting instances of T
        t_ctr += 1
    elif nucleotide == 'C': #counting instances of C
        c_ctr += 1
    else: #counting instances of G
        g_ctr += 1

#printing nucleotides with their respective counts 
#print("A =", a_ctr, ", T =", t_ctr, ", C =", c_ctr, ", G =", g_ctr)
#printing nucleotide counts in the preferred formatting for Rosalind
print(a_ctr, c_ctr, g_ctr, t_ctr)
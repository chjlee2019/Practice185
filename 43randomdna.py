"""
Create a program that generates DNA sequences in FASTA format. 
There should be a variable that controls how many sequences (e.g. 3). 
Each sequence should have a unique identifier (e.g. seq-1) and the length of the sequence should have some random range (e.g 50-60). 
The output should resemble the example below.

>seq-1
GCCGTCTCGGGGGAGAACGAGCGACTGCTGTCCCGGGATGTGCGTAAATGCGGGC
>seq-2
GGTTTTAATAGCACCCGAAGCTCCATCCAGCTAGACGTCGAAGCTTTTTAACACTGTA
>seq-3
CAGTATGGTCCACCCGCCTTTCAGGAATACTTCATCCTAAGTGCCTCGAA
"""

import random

# There should be a variable that controls how many sequences (e.g. 3). 
seqlimit = 10
for i in range(1, seqlimit + 1):
	print (f'>seq-{i}')

# The length of each sequence should have some random range (e.g. 50-60).
	for nt in range(1, 61):
		print(random.choice('ACGT'), end="")
	print()

# end: how to specify a random range so they don't end with evenly 60 nt for all sequences?
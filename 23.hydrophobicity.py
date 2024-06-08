# Write a function that returns the Kyte-Doolittle hydrophobicity value for an amino acid letter. 
# Demonstrate that the function works by calling it multiple times with different letters, one of which should be outside the amino acid alphabet.

def hydrophobicity (aa):

if aa == A:
	print ('1.80')
elif aa == C:
	print ('2.50')
elif aa == D:
	print ('-3.50')
elif aa == E:
	print ('-3.50')
elif aa == F:	
	print ('2.80')
elif aa == G:
	print ('-0.40')
elif aa == H:	
	print ('-3.20')
elif aa == I:
	print ('4.50')
elif aa == K:
	print ('-3.90')
elif aa == L:
	print ('3.80')
elif aa == M:
	print ('1.90')
elif aa == N:
	print ('-3.50')
elif aa == P:
	print ('-1.60')
elif aa == Q:
	print ('-3.50')
elif aa == R:
	print ('-4.50')
elif aa == S:
	print ('-0.80')
elif aa == T:
	print ('-0.70')
elif aa == V:
	print ('4.20')
elif aa == W:
	print ('0.90')
elif aa == Y:
	print ('1.30')
elif aa == W:
	print ('-0.90')
elif aa == Y:
	print ('-1.30')
else:
	print  ('Invalid')
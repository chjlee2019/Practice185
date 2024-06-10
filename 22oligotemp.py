# Oligo Temperature (Tm)

def oligotemp(A, C, G, T):							#define function	
	if A+C+G+T <= 13: return (A+T)*2 + (G+C)*4
	else: return 64.9 + 41*(G+C - 16.4) / (A+T+G+C)
	
print(oligotemp(2, 3, 3, 2))						#assign variable

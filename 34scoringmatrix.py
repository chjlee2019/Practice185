alphabet = 'ACGT'
match = '+1'
mismatch = '-1'

print("  ", end=" ")
for nt in alphabet:
	print(nt, end="  ")
print()

for nt1 in alphabet:
	print(nt1, end=" ")
	for nt2 in alphabet:
		if nt1 == nt2:    print(match, end=" ")
		else:             print(mismatch, end=" ")
	print()
	
#while True:
#	print ('hello')
	
i = 0
while True:
	i = i + 1
	print('hey', i)
	if i ==3: break
	
i = 0
while i < 3:
	print(i)
	i = i + 1
	print('final value of i is', i)
	
i = 1
while i < 10:
	print(i)
	i = i + 3
	print('final value of i is', i)
	
for i in range (1, 10, 3):
	print(i)
	
for i in range(0, 5):
	print(i)

for char in 'hello':
	print(char)

seq = 'ACCTTGA'
for nt in seq:
	print(nt)
	
for nt1 in 'ACGT':
	for nt2 in 'ACGT':
		if nt1 == nt2: print (nt1, nt2, '+1')
		else:		   print (nt1, nt2, '-1')
	
"""
seq = 'CTGATC'
print(seq[0], seq[1])

print(seq[-1])

for nt in seq: print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])



s = 'ABCDEFGHIJ'
print(s[0:5])

print(s[0:8:2])                        #0 = start, 8 = end-before limit, 2 = step size (slice)

print(s[0:5], s[:5])                   #both ABCDE (omit initial value)
print(s[5:len(s)], s[5:])              #both FGHIJ (omit final value)
	
print(s, s[::], s[::1], s[::-1])       #the negative index in s[::-1] reads in reverse.



tax = ('Homo', 'sapiens', 9606)        #construct tuple
print(tax)

#s[0] = 'C'
#tax[0] = 'human'

print(tax[0])                          #index
print(tax[::-1])                       #slice

def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2

x1, x2 = quadratic(5, 6, 1)           # unpacked tuple - yes
print(x1, x2)                         # pretty
intercepts = quadratic(5, 6, 1)       # packed tuple - no
print(intercepts[0], intercepts[1])   #ugly


nts = 'GATC'                          #indices: i
for i in range(len(nts)):             #value: nts
    print(i, nts[i]) 
    
for i, nt in enumerate(nts):
	print(i, nt)


names = ('adenine', 'cytosine', 'guanine', 'thymine')    #container: names, nts
for i in range(len(names)):	
	print(nts[i], names[i])

for nt, name in zip(nts, names):       #container:
	print(nt, name)			           #element:
				                       #tuple:
				                       
for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name)


nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'                            #replaces C (position 0, 1, 2) with G
print(nts)                        

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

nts.copy()

items = list()
print(items)
items.append('broccoli')
print(items)

stuff = []
stuff.append(5)
print(stuff)

text = 'good day   to you'
words = text.split()
print(words)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)
line = '1.41,2.72,3.14'
print(line.split(','))
print(aas)

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))         # report location of 'G'
#print('index Z?', alph.index('Z'))        # not in list, so error

if thing in list: idx = list.index(thing)  # supposed to have error?
"""

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = va
		elif val > maxi: maxi = val
	return mini, maxi
	
def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)                #len(vals) like the sum

import math
def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h
print(entropy([0.2, 0.3, 0.5]))

def dkl(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log2(p/q)
	return d
p1 = [0.5, 0.4, 0.3, 0.2]
p2 = [0.2, 0.3, 0.4, 0.5]
print(dkl(p1, p2))

"""
with open(path) as fp:
    for line in fp:
        do_something_with(line)
        
fp = open(path)
for line in fp:
    do_something_with(line)
fp.close()

import gzip
with gzip.open(path, 'rt') as fp:
    for line in fp:
        print(line, end='')
"""

i = int('42')
x = float('0.61803')      
        
import math 

# na, nc, ng, and nt are the numerical count
def shannon(na, nc, ng, nt):
	tot = na + nc + ng + nt
	pa = na / tot
	pc = nc / tot
	pg = ng / tot
	pt = nt / tot
	h = 0
	if pa != 0: h = h + pa * math.log2(pa)
	if pc != 0: h = h + pc * math.log2(pc)
	if pg != 0: h = h + pg * math.log2(pg)
	if pt != 0: h = h + pt * math.log2(pt)
	ha 
	hc 
	hg 
	nt
	

"""
Common theme:
container:  variable, list, etc.
initialization: h = 0 (dependent on function)


Calculate the Shannon entropy/relative entropy of given distribution(s).

If only probabilities pk are given, the Shannon entropy is calculated as H = -sum(pk * log(pk)).

If qk is not None, then compute the relative entropy D = sum(pk * log(pk / qk)). This quantity is also known as the Kullback-Leibler divergence.
"""	


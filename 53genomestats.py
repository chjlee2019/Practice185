import gzip
import sys
import math                          # just for the sq root.

# Can you access a file and reads its contents?
gffpath = sys.argv[1]                #argument vector 1
feature = sys.argv[2]                #argument vector 2

# You don't edit a program; you just hand it a different file. ex. not rewriting the gzip
# In this case, gffpath specifies the location; feature is what we want to grab - i.e. what are the stats of the genome?
  # ex. features = exons...this is what's contained... and tabulate
lengths = []                                         # populate lists with
with gzip.open(gffpath, 'rt') as fp:                 # sys.argv[1] = 
	for line in fp: 
		if line[0] == '#': continue                         # better to include as throwaway
		words = line.split()
		if words[2] != feature: continue
		beg = int(words[3])                      # convert these 'numbers' (which really aren't) into integers
		end = int(words[4])                      # those integers can then be used to generate our calculations
		lengths.append(end - beg + 1)            # get the length of the gene

# Collect numbers: min, max, stdev, median: can you do descriptive stats? Can you do calculations?

#count (genes in the genome - how many exons are there?)
# count is just the length of lengths: len() = because the # of lengths = the # of genes
for i in len(lengths):
	print(i, lengths[i])


#min and #max (What is minimum length, maximum length?)
def minmax(lengths):
	mini = lengths[0]
	maxi = lengths[0]
	for i in lengths:
		if lengths < mini: mini = val
		if lengths > maxi: maxi = val
	return mini, maxi

#mean (What is the average length?)
def mean(lengths):
	total = 0
	for i in lengths: total += lengths
	return total / len(lengths)

#standard deviation (What is the standard deviation of lengths?)
# From Unit 3: "if you want to compute the standard deviation for a set of numbers, you must iterate through the values, squaring the differences to the mean. Iteration is also called looping."
def stdev(lengths):
	mean = 0
	for i in len(lengths):
	
	return math.sqrt()
	
#median (What is the median length?)
# First, how to sort lengths from smallest to largest value?
def median(lengths):
	median = 0
	n = len(lengths)
	
# Second, how to 
# Probably conditionals apply depending on whether the list has an even or odd number of samples.
	for i in range(lengths):
		if len(lengths) % 2 == 0:  median = ((n/2)+(n/2)+1)/2          # even
		else:                      median = (n+1)/2                    # odd
		return 
	
	


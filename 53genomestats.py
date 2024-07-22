import gzip
import sys
import math                          # just for the sq root.

# Can you access a file and reads its contents?
gffpath = sys.argv[1]                #argument vector 1
feature = sys.argv[2]                #argument vector 2

# You don't edit a program; you just hand it a different file. ex. not rewriting the gzip
# In this case, gffpath specifies the location; feature is what we want to grab - i.e. what are the stats of the genome?
  # ex. features = exons...this is what's contained... and tabulate
lengths = []                                         # populate lists with lengths
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
print(len(lengths))


#min and #max (What is minimum length, maximum length?); for other functions, they're not concerned with lengths - but any number.
def minmax(nums):                          # nums is generic
	mini = nums[0]
	maxi = nums[0]
	for num in nums:
		if num < mini: mini = num
		if num > maxi: maxi = num
	return mini, maxi
	
vals = [3, 8, 4, 1, 12]
low, high = minmax(vals)                 #unpack - Get in the habit of unpacking -better understood by the reader.
#r = minmax(vals)                        #ugly
print(minmax(vals))
print(low, high) 
#print(r[0], r[1])                       #ugly

"""
362 
(1, 12)                                  #pack
1 12                                     #unpack
"""

#mean (What is the average length?)
def mean(nums):
	total = 0
	for num in nums: total += num
	return total / len(nums)

vals = [3, 8, 4, 1, 12]
print(mean(vals))

def mean2(nums):
	total = 0
	for i in range(len(nums)): total += nums[i]      # for any previous value, for i in range
	return total / len(nums)


#standard deviation (What is the standard deviation of lengths?)
# From Unit 3: "if you want to compute the standard deviation for a set of numbers, 
#you must iterate through the values, squaring the differences to the mean.
# Iteration is also called looping."
# Summation is a loop, sub
def stdev(nums):
	avg = mean(nums)                     # mean adds numbers
	total = 0
	for num in nums: 
		total += (num - avg) ** 2        # total will contain all of the differences from the mean
	return math.sqrt((total / len(nums)))
	
def stdev2(nums):
	avg = mean(nums)
	total = 0
	for i in range(len(nums)): 
		total += (nums[i] - avg) ** 2
	return math.sqrt((total / len(nums)))

vals = [3, 8, 4, 1, 12]
print(mean(vals))
	
	
#median (What is the median length?)
def median(nums):
	nums.sort()
	print(nums)
	ind1 = len(nums)//2
	ind2 = ind1 - 1
	if len(nums) % 2 ==1:
		median = nums[ind1]      # odd
	else:	
		median = nums[ind1] + nums[ind2]/2

vals = [4, 3, 5, 2, 1]  		        # call function.
vals = [4, 2, 5, 3]
print(median(vals))  
import dogma

print(dogma.transcribe('ACGT'))
print(dogma.revcomp('AAAACGT'))
print(dogma.revcomp('CAGTTGAC'))        #unit test

print(dogma.translate('ATGTAA'))        #should return M*, with * = stop codon

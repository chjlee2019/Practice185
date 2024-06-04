cd /Code/MCB185/data
gunzip -c dictionary.gz| grep "r" | grep -v "[^zoniacr]" | grep -E ".{4,}"


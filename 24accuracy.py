import math

def performance(tp, tn, fp, fn):
	return accuracy(tp, tn, fp, fn), fscore(tp, tn, fp, fn)
	
def p2(tp, tn, fp, fn):
	return tp + tn / (tp + tn + fp + fn), 2 * (tp / (tp + fp)) * (tp / (tp + fn))

"""
def accuracy(tp, tn, fp, fn):
	return tp + tn / (tp + tn + fp + fn)


def fscore(tp, tn, fp, fn):
	pre = tp / (tp + fp)
	rec = tp / (tp + fn)
	return 2 * (pre * rec) / (pre + rec)
	
print(accuracy(5, 2, 3, 4))
print(fscore(5, 2, 3, 4))
"""

"""
						Predicted	Actual
True Positive  (tp)			+		  +
True Negative  (tn)			-		  -	
False Positive (fp)			+		  -
False Negative (fn)			-		  +

+ (positive) or  - (negative) is a binary 'Yes' or 'No'

accuracy: (sum of true positives and true negatives) / total number of samples 
precision: (true positives) / (sum of true positives and false positives)
recall: (true positives) / (sum of true positives and false negatives)
F1 score: 2 * (precision * recall) / (precision + recall)



main variables:
	tp = 
	tn = 
	fp = 
	fn = 
	total number of samples = tp + tn + fp + fn
	
"""


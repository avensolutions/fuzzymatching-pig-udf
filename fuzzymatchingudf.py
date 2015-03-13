@outputSchema("n:bag{t:tuple(ngram:chararray)}")
def return_ngrams(s,n):
	outBag = []
	if s is None: return None
	input_list = list(s)
	for i in range(len(input_list)-(n-1)):
		ngram_arr = input_list[i:i+n]
		ngram_str = "".join(l.lower() for l in ngram_arr)
		outBag.append(ngram_str)
	return outBag

@outputSchema("q:bag{t:tuple(qgram:chararray)}") 
def return_qgrams(bag_of_ngrams):
	outBag = []
	if bag_of_ngrams is None: return None
	try:
		# first append all ngrams for first tuple
		qgram_str = ""
		for ngram in bag_of_ngrams:
			if ngram is None: continue
			ngram_str = ''.join(ngram)
			qgram_str = qgram_str + ngram_str
		outBag.append(qgram_str)
		# next remove one element position by position and return the remaining elements as one tuple
		input_len = len(bag_of_ngrams)
		for i in range(input_len):
			qgram_str = ""
			ngram_index = 0
			for ngram in bag_of_ngrams:
				if ngram is None: continue
				if ( i != ngram_index ):
					ngram_str = ''.join(ngram)
					qgram_str = qgram_str + ngram_str
				ngram_index = ngram_index+1
			outBag.append(qgram_str)
	except: return None                      
	else: return outBag
                
'''             
/* Pig Usage
test.data :
david
craig
jeffrey
naden
malcolm
mark
stuart
UPPERCASE
MixedCase
StartsWithUpper
*/
REGISTER 'fuzzymatchingudf.py' USING jython as fuzzymatchingudf;
raw_data = LOAD 'test.data' USING PigStorage();
--names_with_ngrams = FOREACH raw_data GENERATE $0, fuzzymatchingudf.return_ngrams($0,3);
--DUMP names_with_ngrams;
names_with_qgrams = FOREACH raw_data GENERATE $0, fuzzymatchingudf.return_qgrams(fuzzymatchingudf.return_ngrams($0,3));
--DUMP names_with_qgrams;
flattened_qgrams = FOREACH names_with_qgrams GENERATE $0, FLATTEN($1);
DUMP flattened_qgrams;
'''


import fuzzymatchingudf
print "Enter ngram size:",
ngram_size_str = raw_input()
ngram_size = int(ngram_size_str)
test_data = open('test.data', 'r')
for name in test_data:
	print 'Input Record : ' + name
	ngrams = fuzzymatchingudf.return_ngrams(name,ngram_size)
	print 'ngrams : ' + str(ngrams)
	qgrams = fuzzymatchingudf.return_qgrams(name,ngram_size)
	print 'qgrams : ' + str(qgrams)
	print '--------'
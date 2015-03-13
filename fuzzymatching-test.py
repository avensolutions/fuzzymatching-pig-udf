import os

# prepare temp udf module without outputSchema decorators
tmpfile = 'fuzzymatchingudftmp.py'
if os.path.exists(tmpfile):
	os.remove(tmpfile)
f = open(tmpfile, 'w')
file = open('fuzzymatchingudf.py', 'r')
for line in file:
	line_str = str(line)
	if not line_str.startswith('@'):
		f.write(line)
f.close()

import fuzzymatchingudftmp
print "Enter ngram size:",
ngram_size_str = raw_input()
ngram_size = int(ngram_size_str)
test_data = open('test.data', 'r')
for name in test_data:
	print 'Input Record : ' + name
	ngrams = fuzzymatchingudftmp.return_ngrams(name,ngram_size)
	print 'ngrams : ' + str(ngrams)
	qgrams = fuzzymatchingudftmp.return_qgrams(ngrams)
	print 'qgrams : ' + str(qgrams)
	print '--------'
import os

# prepare temp udf module without outputSchema decorators
tmpfile = "fuzzymatchingudftmp.py"
if os.path.exists(tmpfile):
	os.remove(tmpfile)
f = open(tmpfile, 'w')
file = open('fuzzymatchingudf.py', 'r')
for line in file:
	line_str = str(line)
	if not line_str.startswith("@"):
		f.write(line)
f.close()

import fuzzymatchingudftmp
print "Enter a name:",
name = raw_input()
print "Name entered: " + name
outbag = fuzzymatchingudftmp.return_ngrams(name,3)
print outbag
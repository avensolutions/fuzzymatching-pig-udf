import fuzzymatchingudf
print "Enter a name:",
name = raw_input()
print "Enter N value:",
N = raw_input()
outbag = fuzzymatchingudf.return_ngrams(name,N)
print outbag
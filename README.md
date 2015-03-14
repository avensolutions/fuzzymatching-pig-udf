# fuzzymatching-pig-udf

Apache Pig UDF to return n-grams and q-grams used for approximate string matching

## Pig Usage

	REGISTER 'fuzzymatchingudf.py' USING jython as fuzzymatchingudf;
	raw_data = LOAD 'test.data' USING PigStorage();
	names_with_ngrams = FOREACH raw_data GENERATE $0, fuzzymatchingudf.return_ngrams($0,3);
	DUMP names_with_ngrams;
	
	names_with_qgrams = FOREACH raw_data GENERATE $0, fuzzymatchingudf.return_qgrams($0,3);
	DUMP names_with_qgrams;
	
	flattened_qgrams = FOREACH names_with_qgrams GENERATE $0, FLATTEN($1);
	DUMP flattened_qgrams;

![fuzzymatching-udf-pig-dump screenshot](http://avensolutions-images.s3-website-us-east-1.amazonaws.com/fuzzymatching-udf-pig-dump-screenshot.png)
	
## Python Test Usage

	python fuzzymatching-test.py
	
![fuzzymatching-udf-python-test-program screenshot](http://avensolutions-images.s3-website-us-east-1.amazonaws.com/fuzzymatching-udf-python-test-program.png)	
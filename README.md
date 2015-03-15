# fuzzymatching-pig-udf

Python (Jython) UDF to return n-grams and q-grams used for approximate string matching
Can be used with Apache Pig, Spark (PySpark) and native Python

## Pig Usage

	REGISTER 'fuzzymatchingudf.py' USING jython as fuzzymatchingudf;
	raw_data = LOAD 'test.data' USING PigStorage();
	names_with_ngrams = FOREACH raw_data GENERATE $0, fuzzymatchingudf.return_ngrams($0,3);
	DUMP names_with_ngrams;
	
	names_with_qgrams = FOREACH raw_data GENERATE $0, fuzzymatchingudf.return_qgrams($0,3);
	DUMP names_with_qgrams;
	
	flattened_qgrams = FOREACH names_with_qgrams GENERATE $0, FLATTEN($1);
	DUMP flattened_qgrams;

## PySpark Usage

	Welcome to
		  ____              __
		 / __/__  ___ _____/ /__
		_\ \/ _ \/ _ `/ __/  '_/
	   /__ / .__/\_,_/_/ /_/\_\   version 1.2.0
		  /_/

	Using Python version 2.6.6 (r266:84292, Feb 22 2013 00:00:18)
	SparkContext available as sc.
	>>>import fuzzymatchingudf
	>>>recs = sc.textFile('test.data')
	>>>ngrams = recs.flatMap(lambda x: fuzzymatchingudf.return_ngrams(x, 2))
	>>>ngrams.collect()
	['da', 'av', 'vi', 'id', 'cr', 'ra', 'ai', 'ig', 'je', 'ef', 'ff', 'fr', 're', 'ey', 'na', 'ad', 'de', 'en', 'ma', 'al', 'lc', 
	'co', 'ol', 'lm', 'ma', 'ar', 'rk', 'st', 'tu', 'ua', 'ar', 'rt', 'up', 'pp', 'pe', 'er', 'rc', 'ca', 'as', 'se', 'mi', 
	'ix', 'xe', 'ed', 'dc', 'ca', 'as', 'se', 'st', 'ta', 'ar', 'rt', 'ts', 'sw', 'wi', 'it', 'th', 'hu', 'up', 'pp', 'pe', 'er']
	
## Native Python Usage

	>>>import fuzzymatchingudf
	>>>print fuzzymatchingudf.return_ngrams("LoremIpsum",2)
	['lo', 'or', 're', 'em', 'mi', 'ip', 'ps', 'su', 'um']
	>>>print fuzzymatchingudf.return_qgrams("LoremIpsum",2)
	['loorreemmiippssuum', 'orreemmiippssuum', 'loreemmiippssuum', 'looremmiippssuum',
	'loorremiippssuum', 'loorreemippssuum', 'loorreemmipssuum', 'loorreemmiipsuum', 
	'loorreemmiippsum', 'loorreemmiippssu']
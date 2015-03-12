REGISTER 'fuzzymatchingudf.py' USING jython as fuzzymatchingudf;
raw_data = LOAD 'test.data' USING PigStorage();
--names_with_ngrams = FOREACH raw_data GENERATE $0, fuzzymatchingudf.return_ngrams($0,3);
--DUMP names_with_ngrams;
names_with_qgrams = FOREACH raw_data GENERATE $0, fuzzymatchingudf.return_qgrams(fuzzymatchingudf.return_ngrams($0,3));
--DUMP names_with_qgrams;
flattened_qgrams = FOREACH names_with_qgrams GENERATE $0, FLATTEN($1);
DUMP flattened_qgrams;
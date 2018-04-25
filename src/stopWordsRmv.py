# coding: utf-8
import sys, codecs, re

def stopWordsRemoval(line):
	"""
	A function to remove stop words

	returns: a list of words excluding stop words
	"""
	words = re.findall(r'\S+|\n',line)
	for word in words:
		if word in stopWordsList:
			words.remove(word)
	return words
	

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print ("Usage: python stopWordsRmv.py <infile> <outfile>")
		sys.exit(1)

	with codecs.open('stopWords.txt','r','utf-8') as stopwords:
		stopWordsList = stopwords.read().splitlines()

	with codecs.open(sys.argv[1],'r','utf-8') as ipfile:
		with codecs.open(sys.argv[2],'w','utf-8') as opfile:
			for line in ipfile.readlines():
				sep = ' '
				stopWords_processed = sep.join(stopWordsRemoval(line))
				opfile.write(stopWords_processed)

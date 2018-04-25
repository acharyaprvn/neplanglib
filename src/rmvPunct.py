# coding: utf-8
import sys, codecs, re

punctList = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '/', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '‘', '’', '“', '”']

def punctListToString():
	"""
	A function that converts the puncuations List into a string

	returns: a string
	"""
	punctString = ''.join(punctList)	
	return punctString

def rmvPunctuation(line):
	"""
	A function to remove punctuation

	returns: a list of words excluding the punctuations
	"""

	#replace tab and additional spaces
	processed_line = re.sub(r'[ \t]+', ' ', line)
	punct = punctListToString()
	pattern = r'([' + re.escape(punct) + r'])'
	rmv_pattern =  re.compile(pattern)
	processed_line = rmv_pattern.sub(r'', processed_line)
	return processed_line.split()
	

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print ("Usage: python rmvPunct.py <infile> <outfile>")
		sys.exit(1)

	with codecs.open(sys.argv[1],'r','utf-8') as ipfile:
		with codecs.open(sys.argv[2],'w','utf-8') as opfile:
			for line in ipfile.readlines():
				sep = ' '
				removed_punct = sep.join(rmvPunctuation(line))
				opfile.write(removed_punct)


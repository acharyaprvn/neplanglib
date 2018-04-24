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

def tokenizer(line):
	"""
	A tokenizer that tokenizes in punctuation boundaries for Nepali language

	returns: a list of tokens
	"""
	
	punct = punctListToString()
	pattern = r'([' + re.escape(punct) + r'])'
	tok_pattern =  re.compile(pattern)
	tok_line = tok_pattern.sub(r' \1 ', line)
	#replace tab and additional spaces
	processed_line = re.sub(r'[ \t]+', ' ', tok_line)
	return processed_line.strip(' ').split()
	

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print ("Usage: python tokenize.py <infile> <outfile>")
		sys.exit(1)

	with codecs.open(sys.argv[1],'r','utf-8') as ipfile:
		with codecs.open(sys.argv[2],'w','utf-8') as opfile:
			for line in ipfile.readlines():
				sep = ' '
				tokenized_line = sep.join(tokenizer(line))
				opfile.write(tokenized_line)


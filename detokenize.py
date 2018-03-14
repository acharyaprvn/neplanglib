# coding: utf-8
import sys, codecs, re

punctGroup1 = '!%,;?)}]|'
punctGroup2 = '({['
punctGroup3 = '/'

def leftSpaceRemoval(line):
	pattern = r'\s([' + re.escape(punctGroup1) + r'])'
	detok_pattern =  re.compile(pattern)
	detok_line = detok_pattern.sub(r'\1', line)
	#print (detok_line)
	return detok_line


def detokenizer(line):
	"""
	A detokenzer that detokenizes in punctuation boundaries for Nepali language

	returns: a detokenized string
	"""
	#replace tab and additional spaces
	processed_line = re.sub(r'[ \t]+', ' ', line)
	
	

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print ("Usage: python detokenize.py <infile> <outfile>")
		sys.exit(1)

	with codecs.open(sys.argv[1],'r','utf-8') as ipfile:
		with codecs.open(sys.argv[2],'w','utf-8') as opfile:
			for line in ipfile.readlines():
				opfile.write(detokenizer(line)+'\n')


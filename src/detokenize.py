# coding: utf-8
import sys, codecs, re

punctGroup1 = '!%,;?)}]|'
punctGroup2 = '({['
punctGroup3 = '/'

def leftSpaceRemoval(line):
	pattern = r'\s([' + re.escape(punctGroup1) + r'])'
	detok_pattern =  re.compile(pattern)
	detok_line = detok_pattern.sub(r'\1', line)
	return detok_line


def rightSpaceRemoval(line):
	pattern = r'([' + re.escape(punctGroup2) + r'])\s'
	detok_pattern =  re.compile(pattern)
	detok_line = detok_pattern.sub(r'\1', line)
	return detok_line

def bothSpaceRemoval(line):
	pattern = r'\s([' + re.escape(punctGroup3) + r'])\s'
	detok_pattern =  re.compile(pattern)
	detok_line = detok_pattern.sub(r'\1', line)
	return detok_line

def quotesProcess(line):
	singleQuotesCount = 0
	doubleQuotesCount = 0
	lineToList = line.split()
	#print (lineToList)
	space = ' '
	detokLine = ''
	for word in lineToList:
		if word == "'":
			if singleQuotesCount % 2 == 0:
				detokLine += space + word
				space = ''
			else:
				detokLine += word
				space = ' '
			singleQuotesCount += 1

		elif word == '"':
			if doubleQuotesCount %2 == 0:
				detokLine += space + word
				space = ''
			else:
				detokLine += word
				space = ' '
			doubleQuotesCount += 1

		else:
			detokLine += space + word
			space = ' '
	return detokLine.strip()

def detokenizer(line):
	"""
	A detokenzer that detokenizes in punctuation boundaries for Nepali language

	returns: a list of detokenized words
	"""
	#replace tab and additional spaces
	processed_line = re.sub(r'[ \t]+', ' ', line)
	quotes = quotesProcess(processed_line)	
	leftSpaceProcessed = leftSpaceRemoval(quotes)
	rightSpaceProcessed = rightSpaceRemoval(leftSpaceProcessed)
	bothSpaceProcessed = bothSpaceRemoval(rightSpaceProcessed)
	return bothSpaceProcessed.split()

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print ("Usage: python detokenize.py <infile> <outfile>")
		sys.exit(1)

	with codecs.open(sys.argv[1],'r','utf-8') as ipfile:
		with codecs.open(sys.argv[2],'w','utf-8') as opfile:
			for line in ipfile.readlines():
				sep = ' '
				detokenized_line = sep.join(detokenizer(line))
				opfile.write(detokenized_line)


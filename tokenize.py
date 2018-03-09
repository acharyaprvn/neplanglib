import sys, codecs, string, re

punctList = [x for x in string.punctuation]

def addPunct():
	"""
	A function to add additional punctuations other than standard English punctuations provided by string.punctuation
	"""
	newPunctList = ['|']
	for x in newPunctList:
		punctList.append(x)


def removePunct():
	"""
	A function to remove unnecessary punctuations provided by string.punctuation
	"""
	delPunctList = ['.',':','-']
	for x in delPunctList:
		punctList.remove(x)


def punctListToString():
	"""
	A function that adds, removes and converts the puncuations List into a string

	returns: a string
	"""
	addPunct()
	removePunct()
	punctString = ''.join(punctList)	
	return punctString

def tokenize(line):
	"""
	A tokenzer that tokenizes in punctuation boundaries for Nepali language

	returns: a list of tokens
	"""
	
	punct = punctListToString()
	pattern = r'([' + re.escape(punct) + r'])'
	tok_pattern =  re.compile(pattern)
	tok_line = tok_pattern.sub(r' \1 ', line)
	#replace tab and additional spaces
	processed_line = re.sub(r'[ \t]+', ' ', tok_line)
	return processed_line.strip(' ').split(' ')
	

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print "Usage: python tokenize.py <infile> <outfile>"
		sys.exit(1)

	with codecs.open(sys.argv[1],'r','utf-8') as ipfile:
		with codecs.open(sys.argv[2],'w','utf-8') as opfile:
			for line in ipfile.readlines():
				sep = ' '
				tokenized_line = sep.join(tokenize(line))
				opfile.write(tokenized_line)


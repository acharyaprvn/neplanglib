import sys, codecs, string, re


def tokenize(line):
	"""

	"""
	punctuations = string.punctuation.replace('.','')
	pattern = r'([' + re.escape(punctuations) + u"\u0964" + r'])'
	tok_pattern =  re.compile(pattern)
	tok_line = tok_pattern.sub(r' \1 ', line)

	#replace tab and additional spaces
	processed_line = re.sub(r'[ \t]+', ' ', tok_line)
	#print(tok_str)
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


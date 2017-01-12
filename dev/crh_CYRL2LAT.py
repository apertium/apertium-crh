#!/usr/bin/env python3

import sys;

tt = {
	'къ':'q',
	'нъ':'ñ',
	'гъ':'ğ',
	'дж':'c',
	'а':'a',
	'б':'b',
	'в':'v',
	'г':'g',
	'д':'d',
	'е':'e',
	'ё':'yo',
	'ж':'j',
	'з':'z',
	'и':'i',
	'й':'y',
	'к':'k',
	'л':'l',
	'м':'m',
	'н':'n',
	'o':'o',
	'п':'p',
	'р':'r',
	'c':'s',
	'т':'t',
	'у':'u',
	'ф':'f',
	'х':'h',
	'ц':'ts',
	'ч':'ç',
	'ш':'ş',
	'щ':'ş',
	'ъ':'',
	'ы':'ı',
	'ь':'',
	'э':'e',
	'ю':'yu',
	'я':'ya'
};

def main(i, o, tt): #{
	k = list(tt.keys());
	for line in i.readlines(): #{
		for s in sorted(tt, key=len, reverse=True): #{
			line = line.replace(s, tt[s]);
			line = line.replace(s.upper(), tt[s].upper());
		#}
		o.write(line);
	#}	
	
#}

if __name__ == "__main__": #{
	main(sys.stdin, sys.stdout, tt);
#}

#!/usr/bin/env python3

import sys;

ZERO = '.*'

tt = {
	('нъ', ZERO):'ñ',
	('дж', ZERO):'c',
	('а', ZERO):'a',
	('б', ZERO):'b',
	('в', ZERO):'v',
	('г', ZERO):'g',
	('д', ZERO):'d',
	('ж', ZERO):'j',
	('з', ZERO):'z',
	('и', ZERO):'i',
	('й', ZERO):'y',
	('к', ZERO):'k',
	('л', ZERO):'l',
	('м', ZERO):'m',
	('н', ZERO):'n',
	('п', ZERO):'p',
	('р', ZERO):'r',
	('с', ZERO):'s',
	('т', ZERO):'t',
	('ф', ZERO):'f',
	('х', ZERO):'h',
	('ч', ZERO):'ç',
	('ш', ZERO):'ş',
	('щ', ZERO):'ş',
	('ы', ZERO):'ı',
	('э', ZERO):'e',
	('ц', ZERO):'ts',

	('къ', ZERO):'q',
	('гъ', ZERO):'ğ',
	('ъ', ZERO):'',
	('ь', ZERO):'',
	'o':'o',  # o, ö
	'у':'u',  # u, ü
	'е':'ye', # ye, e
	'ё':'yo', # yo, ö, yö
	'ю':'yu', # yu, ü, yü
	'я':'ya'  # ya, â, 
};

#             Front  First

FrontVow = '[еиэ]'; # non 1st syll.
BackVow = '[аоу]'; # non 1st syll.
Back = '(' + BackVow + '|' + '[кг]ъ)';      # ([аоу]|[кг]ъ)
Front = '(' + FrontVow + '|' + 'кг[^ъ]|ь)'; # ([еиэ]|[кг][^ъ]|ь)
Vow = '[аеиоуэюя]';
Cns = '[^аеиоуэюя]';

Unspec = '(б|в|д|дж|ж|з|л|м|н|нъ|п|р|с|т|ф|x|ц|ч|ш|щ|ю|ё)*'

# ю(б|в|д|дж|ж|з|л|м|н|нъ|п|р|с|т|ф|x|ц|ч|ш|щ|ю|ё)*([аоу]|[кг]ъ)
# ю(б|в|д|дж|ж|з|л|м|н|нъ|п|р|с|т|ф|x|ц|ч|ш|щ|ю|ё)*([еиэ]|[кг][^ъ]|ь)

FrontContext = Unspec + Front ;
BackContext = Unspec + Back ;

# ю зюни
# yüzüni

v = {	
	('ю', ):'yü',
	('ю', FRONT, not FIRST): 'ü',
	('ю', not FRONT, FIRST): 'yu',
	('ю', not FRONT, not FIRST): 'yu',
);

def main(i, o, tt): #{
	k = list(tt.keys());
	for line in i.readlines(): #{
		row = line.split(' ');
		for j in row: #{
			for s in sorted(tt, key=len, reverse=True): #{
				row[j] = row[j].replace(s, tt[s]);
				row[j] = row[j].replace(s.upper(), tt[s].upper());
			#}
		#}
		o.write(' '.join(row));
	#}	
	
#}

if __name__ == "__main__": #{
	main(sys.stdin, sys.stdout, tt);
#}

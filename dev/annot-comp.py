import sys ;

old = open(sys.argv[1]);
new = open(sys.argv[2]);

found = [];

for blokk in old.read().split('\n\n'): #{

	f = blokk.split('\n')[0];
	found.append(f);
#}

for blokk in new.read().split('\n\n'): #{

	
	f = blokk.split('\n')[0];
	if f not in found: #{
		print(blokk);
		print('')
	#}
#}

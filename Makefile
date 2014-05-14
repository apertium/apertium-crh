all:
	hfst-lexc -v apertium-crh.crh.lexc -o crh.lexc.hfst
	hfst-twolc apertium-crh.crh.twol -o crh.twol.hfst
	hfst-compose-intersect -1 crh.lexc.hfst -2 crh.twol.hfst -o crh.hfst
	hfst-invert crh.hfst | hfst-fst2txt > crh.automorf.att
	hfst-fst2txt crh.hfst > crh.autogen.att
	lt-comp lr crh.automorf.att crh.automorf.bin
	lt-comp lr crh.automorf.att crh.autogen.bin

clean:
	rm *.bin *.att *.hfst

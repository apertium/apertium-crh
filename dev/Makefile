# Check ../.deps/crh.LR.hfst because error
all: lat2cyrl cyrl2lat 
	#hfst-compose-intersect -1 ../.deps/crh.LR.hfst -2 crh_LAT2CYRL.ngrams.hfst -o crh.LR.cyrl.hfst
	hfst-compose -1 ../.deps/crh.LR.hfst -2 crh_LAT2CYRL.ngrams.hfst -o crh.LR.cyrl.hfst
	hfst-union -1 ../.deps/crh.LR.hfst -2 crh.LR.cyrl.hfst -o crh.LR.biscript.hfst
	hfst-invert crh.LR.biscript.hfst | hfst-fst2fst -w -o crh.LR.biscript.hfstol

test:
	@bash crh_CYRL2LAT.sh
	@bash crh_LAT2CYRL.sh

cyrl2lat:
	hfst-twolc -i crh_CYRL2LAT.twol -o crh_CYRL2LAT.twol.hfst
	hfst-lexc crh_CYRL2LAT.lexc -o crh_CYRL2LAT.lexc.hfst
	hfst-compose-intersect -1 crh_CYRL2LAT.lexc.hfst -2 crh_CYRL2LAT.twol.hfst -o crh_CYRL2LAT.hfst
	hfst-fst2fst -w -i crh_CYRL2LAT.hfst -o crh_CYRL2LAT.hfstol

lat2cyrl:
	hfst-twolc -i crh_LAT2CYRL.twol -o crh_LAT2CYRL.twol.hfst
	hfst-lexc crh_LAT2CYRL.lexc -o crh_LAT2CYRL.lexc.hfst
	hfst-compose-intersect -1 crh_LAT2CYRL.lexc.hfst -2 crh_LAT2CYRL.twol.hfst -o crh_LAT2CYRL.hfst
	cat crh_CYRL.txt | hfst-strings2fst -j | hfst-minimise -o crh_CYRL.words.hfst
	hfst-compose -1 crh_LAT2CYRL.hfst -2 crh_CYRL.words.hfst -o crh_LAT2CYRL.words.hfst
	cat ngrams/crh_CYRL.ngrams.2.tsv | hfst-strings2fst -j | hfst-repeat -f 1 -o crh_CYRL.ngrams.hfst
	#cat ngrams/crh_CYRL.ngrams.3.tsv | hfst-strings2fst -j | hfst-repeat -f 1 -o crh_CYRL.ngrams.hfst
	##cat ngrams/crh_CYRL.ngrams.5.tsv | hfst-strings2fst -j | hfst-repeat -f 1 -o crh_CYRL.ngrams.hfst
	hfst-compose -1 crh_LAT2CYRL.hfst -2 crh_CYRL.ngrams.hfst | hfst-minimise -E -o crh_LAT2CYRL.ngrams.hfst
	#hfst-fst2fst -w crh_LAT2CYRL.ngrams.hfst -o crh_LAT2CYRL.hfstol
	#hfst-union -1 crh_LAT2CYRL.hfst -2 crh_LAT2CYRL.words.hfst| hfst-fst2fst -w -o crh_LAT2CYRL.hfstol
	hfst-union -1 crh_LAT2CYRL.ngrams.hfst -2 crh_LAT2CYRL.words.hfst | hfst-fst2fst -w -o crh_LAT2CYRL.hfstol

clean:
	rm *.hfst *.hfstol

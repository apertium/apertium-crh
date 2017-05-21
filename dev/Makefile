all: lat2cyrl cyrl2lat test
	hfst-compose-intersect -1 ../.deps/crh.LR.hfst -2 crh_LAT2CYRL.hfst -o crh.LR.cyrl.hfst
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
	hfst-union -1 crh_LAT2CYRL.hfst -2 crh_LAT2CYRL.words.hfst | hfst-fst2fst -w -o crh_LAT2CYRL.hfstol

clean:
	rm *.hfst *.hfstol

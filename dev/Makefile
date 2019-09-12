# Check ../.deps/crh.LR.hfst because error
all: crh-biscript.automorf.bin

crh.LR.biscript.hfstol: crh_CYRL2LAT.hfstol crh_LAT2CYRL.unioned.hfst crh.automorf.CYRL+LAT.hfstol
	#hfst-compose-intersect -1 ../.deps/crh.LR.hfst -2 crh_LAT2CYRL.ngrams.hfst -o crh.LR.cyrl.hfst
	hfst-compose -1 ../.deps/crh.LR.hfst -2 crh_LAT2CYRL.ngrams.hfst -o crh.LR.cyrl.hfst
	hfst-union -1 ../.deps/crh.LR.hfst -2 crh.LR.cyrl.hfst -o crh.LR.biscript.hfst
	hfst-invert crh.LR.biscript.hfst | hfst-fst2fst -w -o crh.LR.biscript.hfstol

crh-biscript.automorf.att.gz: crh.LR.biscript.hfstol
	hfst-fst2txt $< | gzip -9 -c -n > $@

crh-biscript.automorf.bin: crh-biscript.automorf.att.gz ../.deps/.d
	zcat < $< > ../.deps/crh-biscript.automorf.att
	lt-comp lr ../.deps/crh-biscript.automorf.att $@

test:
	@bash crh_CYRL2LAT.sh
	@bash crh_LAT2CYRL.sh

#cyrl2lat:
crh_CYRL2LAT.hfstol:
	hfst-twolc -i crh_CYRL2LAT.twol -o crh_CYRL2LAT.twol.hfst
	hfst-lexc crh_CYRL2LAT.lexc -o crh_CYRL2LAT.lexc.hfst
	hfst-compose-intersect -1 crh_CYRL2LAT.lexc.hfst -2 crh_CYRL2LAT.twol.hfst -o crh_CYRL2LAT.hfst
	hfst-fst2fst -w -i crh_CYRL2LAT.hfst -o crh_CYRL2LAT.hfstol

#lat2cyrl:
crh_LAT2CYRL.unioned.hfst:
	hfst-twolc -i crh_LAT2CYRL.twol -o crh_LAT2CYRL.twol.hfst
	hfst-lexc crh_LAT2CYRL.lexc -o crh_LAT2CYRL.lexc.hfst
	hfst-compose-intersect -1 crh_LAT2CYRL.lexc.hfst -2 crh_LAT2CYRL.twol.hfst -o crh_LAT2CYRL.hfst
	cat crh_CYRL.txt | hfst-strings2fst -j | hfst-minimise -o crh_CYRL.words.hfst
	hfst-compose -1 crh_LAT2CYRL.hfst -2 crh_CYRL.words.hfst -o crh_LAT2CYRL.words.hfst
	cat ngrams/crh_CYRL.ngrams.2.tsv | hfst-strings2fst -j | hfst-repeat -f 1 -o crh_CYRL.ngrams.hfst
	#cat ngrams/crh_CYRL.ngrams.3.tsv | hfst-strings2fst -j | hfst-repeat -f 1 -o crh_CYRL.ngrams.hfst
	##cat ngrams/crh_CYRL.ngrams.5.tsv | hfst-strings2fst -j | hfst-repeat -f 1 -o crh_CYRL.ngrams.hfst
	#cat ngrams/crh_CYRL.ngrams.6.tsv | hfst-strings2fst -j | hfst-repeat -f 1 -o crh_CYRL.ngrams.hfst
	hfst-compose -1 crh_LAT2CYRL.hfst -2 crh_CYRL.ngrams.hfst | hfst-minimise -E -o crh_LAT2CYRL.ngrams.hfst
	#hfst-fst2fst -w crh_LAT2CYRL.ngrams.hfst -o crh_LAT2CYRL.hfstol
	#hfst-union -1 crh_LAT2CYRL.hfst -2 crh_LAT2CYRL.words.hfst| hfst-fst2fst -w -o crh_LAT2CYRL.hfstol
	hfst-union -1 crh_LAT2CYRL.ngrams.hfst -2 crh_LAT2CYRL.words.hfst | hfst-fst2fst -w -o crh_LAT2CYRL.hfstol
	hfst-union -1 crh_LAT2CYRL.ngrams.hfst -2 crh_LAT2CYRL.words.hfst -o crh_LAT2CYRL.unioned.hfst

#combined: lat2cyrl
crh.automorf.CYRL+LAT.hfstol: crh_LAT2CYRL.unioned.hfst
	hfst-compose-intersect -1 ../.deps/crh.LR.hfst -2 crh_LAT2CYRL.unioned.hfst -o ../.deps/crh.LR.CYRL.hfst
	hfst-invert ../.deps/crh.LR.CYRL.hfst > ../.deps/crh.automorf.CYRL.hfst
	hfst-invert ../.deps/crh.LR.hfst | hfst-union -1 - -2 ../.deps/crh.automorf.CYRL.hfst > ../.deps/crh.automorf.CYRL+LAT.hfst
	hfst-invert ../.deps/crh.LR.hfst | hfst-union -1 - -2 ../.deps/crh.automorf.CYRL.hfst | hfst-fst2fst -w > ../.deps/crh.automorf.CYRL+LAT.hfstol
	#hfst-invert ../.deps/crh.LR.hfst | hfst-union -1 - -2 ../.deps/crh.automorf.CYRL.hfst | hfst-fst2fst -w > ../.deps/crh.automorf.CYRL+LAT.hfstol
	#hfst-fst2fst -w ../.deps/crh.automorf.CYRL+LAT.hfstol > ../.deps/crh.automorf.CYRL+LAT.hfstol

clean:
	rm *.hfst *.hfstol

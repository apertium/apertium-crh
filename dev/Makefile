
all:
	hfst-twolc -i crh_CYRL2LAT.twol -o crh_CYRL2LAT.twol.hfst
	hfst-lexc crh_CYRL2LAT.lexc -o crh_CYRL2LAT.lexc.hfst
	hfst-compose-intersect -1 crh_CYRL2LAT.lexc.hfst -2 crh_CYRL2LAT.twol.hfst -o crh_CYRL2LAT.hfst
	hfst-fst2fst -w -i crh_CYRL2LAT.hfst -o crh_CYRL2LAT.hfstol
	@bash crh_CYRL2LAT.sh

clean:
	rm *.hfst *.hfstol

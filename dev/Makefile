
all:
	hfst-twolc -i crh_CYRL2LAT.twol -o crh_CYRL2LAT.hfst
	hfst-twolc -i crh_CYRL2LAT.twol | hfst-fst2fst -O -o crh_CYRL2LAT.hfstol
	@bash crh_CYRL2LAT.sh

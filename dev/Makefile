
all:
	hfst-twolc -i crh_CYRL2LAT.twol -o crh_CYRL2LAT.hfst
	hfst-twolc -i crh_CYRL2LAT.twol | hfst-fst2fst -O -o crh_CYRL2LAT.hfstol
	@for i in `cat crh_CYRL2LAT.twol | grep '!!' | sed 's/ /_/g'`; do w=`echo $$i | sed 's/_/ /g'`; echo $$w | cut -f1 -d':' | sed 's/!! //g' | hfst-strings2fst | hfst-compose-intersect -2 crh_CYRL2LAT.hfst | hfst-fst2strings | sed "s/$$/\t$$w/g"; done

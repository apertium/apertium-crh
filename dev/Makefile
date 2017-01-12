
all:
	hfst-twolc -i crh_CYRL2LAT.twol -o crh_CYRL2LAT.hfst
	@for i in `cat crh_CYRL2LAT.twol | grep '!@' | sed 's/ /_/g'`; do w=`echo $$i | sed 's/_/ /g'`; echo $w | hfst-pair-test crh_CYRL2LAT.hfst | sed "s/$$/\t$$w/g"; done

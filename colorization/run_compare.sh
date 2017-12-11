#!/bin/bash


picsdir=$1
crop="${picsdir}crop.jpg"
bw="${picsdir}bw.png"
tess="${picsdir}tess.png"
bwres="${picsdir}bwres.png"
tessres="${picsdir}tessres.png"
tessrescrop="${picsdir}tessrescrop.png"
python ../flip_tess.py -img_in $crop -img_out $1
python colorization/colorize.py -img_in $bw -img_out $bwres
python colorization/colorize.py -img_in $tess -img_out $tessres
python ../crop_tess.py -img_in $tessres -img_out $tessrescrop

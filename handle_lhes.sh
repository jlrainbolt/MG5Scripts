#!/bin/bash
export TERM=dumb

filepath="$1"
filename="results.txt"
filename="$filepath$filename"
scriptpath="/tthome/jaj710/BranchingFraction/OnlyMuon/Source/"
scriptname="fiducial_acc.py"
events="Events/"
lhename="/unweighted_events"
lhe=".lhe"
gz=".gz"
outfile="acceptance_results.txt"

echo "# MU g cross error Nb_pass_M4l Nb_pass_all" > $outfile

# Copy file over, unzip, calculate acceptance
sed 1d $filename | while read -r run tag cross error nevents
do
    echo "Processing $tag events..."
    MU=${tag:3:2}
    g="0${tag:12:3}"
    thisfile="$tag$lhe"
    cp "$filepath$events$run$lhename$lhe$gz" "$thisfile$gz"
    gunzip "$thisfile$gz"
    acceptance=$(python "$scriptpath$scriptname" $thisfile)
    rm $thisfile
    echo "$MU $g $cross $error $acceptance" >> $outfile
done

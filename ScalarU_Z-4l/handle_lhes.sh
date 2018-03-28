#!/bin/bash
export TERM=dumb

filename="$1"
# filepath="$1"
# filename="results.txt"
# filename="$filepath$filename"
# scriptpath="~/work/BranchingFraction/OnlyMuon/Source/"
scriptpath="/uscms/homes/j/jrainbol/work/BranchingFraction/Exclusion/Source/"
scriptname="fiducial_acc.py"
events="Events/"
lhename="/unweighted_events"
lhe=".lhe"
gz=".gz"
outfile="acceptance_results.txt"

echo "# MU g width error Nb_pass_M4l Nb_pass_all" > $outfile

# Copy file over, unzip, calculate acceptance
sed 1d $filename | while read -r run tag width error nevents
do
    echo "Processing $tag events..."
    MU=${tag:3:2}
    g="0${tag:8:3}"
    thisfile="$tag$lhe"
    cp "$filepath$events$run$lhename$lhe$gz" "$thisfile$gz"
    gunzip "$thisfile$gz"
    acceptance=$(python "$scriptpath$scriptname" $thisfile)
    rm $thisfile
    echo "$MU $g $width $error $acceptance" >> $outfile
done

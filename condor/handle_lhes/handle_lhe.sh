#!/bin/bash
export TERM=dumb

lhepath="/tthome/jaj710/MG5_aMC_v2_6_1/ScalarU_gUbmu-0/Events/"
lhename="unweighted_events.lhe"
scriptname="fiducial_acc.py"
outfile="acceptance_results.txt"

run="$1""/"
tag="$2"
cross="$3"
error="$4"
nevents="$5"

MU=${tag:3:2}
g="0${tag:11:3}"

echo "Processing $tag events..."

cp "$lhepath$run$lhename"".gz" .
gunzip "$lhename"".gz"
acceptance=$(python "$scriptname" "$thisfile")
rm "$lhename"
echo "$MU $g $cross $error $acceptance" >> "$outfile"

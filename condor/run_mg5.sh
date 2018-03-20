#! /bin/sh

home="/tthome/jaj710/"
runpath="MG5Scripts/condor/"
mg5path="MG5_aMC_v2_6_1/"
runfile="mg5_run.txt"

output="condor_test/" #"ScalarU_gUbmu-0/"
tarball="tarball.tar.gz"

MU="$1"
gUbe="$2"
gUbmu="$3"

echo "host is " $HOSTNAME
echo "location is " $TEMP
date

echo " "
echo " Copy contents of MG5 directory to $TEMP"
echo " "
pwd
cp "$home$mg5path$output$tarball" .
tar -xzf "$tarball"
ls
#cp "$home$runpath""run_card.dat" Cards/.
#cp "$home$runpath""param_card.dat" Cards/.
#cat Cards/run_card.dat

echo " "
echo " Write MG5 input text file "
echo " "
cp "$home$runpath""write_mg5_run.py" .
python "write_mg5_run.py" "$MU" "$gUbe" "$gUbmu"
#cat "$runfile"

echo " "
echo " Generate events "
echo " "
./bin/madevent "$runfile"

echo "Finished."
date

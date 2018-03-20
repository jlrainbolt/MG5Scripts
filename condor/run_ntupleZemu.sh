#! /bin/sh
echo "host is " $HOSTNAME
echo "location is " $TEMP
date

echo " "
echo " Set up root, etc. "
echo " "
export SCRAM_ARCH=slc6_amd64_gcc491
source /software/tier3/osg/cmsset_default.sh
cd /tthome/schmittm/TEST/CMSSW_7_4_12/src 
cmsenv
echo "ROOTSYS = " $ROOTSYS

echo " "
echo " Return to temporary disk " $TEMP
echo " "
cd $TEMP
pwd

cp /tthome/schmittm/CMS/Zemu/BACON/2012/ntuplesZemu.C .
cp /tthome/schmittm/CMS/Zemu/BACON/2012/R*.hh .
cp /tthome/schmittm/CMS/Zemu/BACON/2012/list*txt  .
ls -l
ln -s /tthome/schmittm/TEST/CMSSW_7_4_12/BaconAna-Run1/ BaconAna
ls -l BaconAna/DataFormats/interface/

echo " "
echo " Check which input source "
echo " "
grep "const Int_t ISRC" ntuplesZemu.C

echo " "
echo " Run macro "
echo " "

root.exe -q -b ntuplesZemu.C

echo " "
echo " Look at the root files "
echo " "
ls -l *.root

echo " "
echo " Move product to shared area "
echo " "
mv -v ski*root  /tthome/share/michael/

echo " "
echo " Delete leftover files "
echo " "
rm -fv list*txt
rm -fv ntuplesZemu.C
rm -fv R*.hh

echo "Finished."
date


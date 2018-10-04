#!/bin/bash

start=`date +%s`

export SCRAM_ARCH=slc6_amd64_gcc630
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

# -- CMSSW enviornment -- #
cd /cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_10_1_9 # -- has NNPDF3.1+luxQED PDF set
eval `scramv1 runtime -sh` # -- cmsenv

cd /home/kplee/Physics/FEWZ/v03_absRapCut/FEWZ_3.1.rc/bin

echo "run: ./local_run.sh z v20181002_TestForBinOpti_M60to120_diRap3.0to4.0_NLO v20181002_TestForBinOpti_M60to120_diRap3.0to4.0_NLO_param.txt v20181002_TestForBinOpti_M60to120_diRap3.0to4.0_NLO_hist.txt v20181002_TestForBinOpti_M60to120_diRap3.0to4.0_NLO.dat ../ 1"
./local_run.sh z v20181002_TestForBinOpti_M60to120_diRap3.0to4.0_NLO v20181002_TestForBinOpti_M60to120_diRap3.0to4.0_NLO_param.txt v20181002_TestForBinOpti_M60to120_diRap3.0to4.0_NLO_hist.txt v20181002_TestForBinOpti_M60to120_diRap3.0to4.0_NLO.dat ../ 1

echo "run: ./finish.sh v20181002_TestForBinOpti_M60to120_diRap3.0to4.0_NLO NLO.v20181002_TestForBinOpti_M60to120_diRap3.0to4.0_NLO.dat"
./finish.sh v20181002_TestForBinOpti_M60to120_diRap3.0to4.0_NLO NLO.v20181002_TestForBinOpti_M60to120_diRap3.0to4.0_NLO.dat

echo "job is completed"

end=`date +%s`

runtime=$((end-start))

echo "   start:   "$start
echo "   end:     "$end
echo "   runtime: "$runtime


#!/bin/bash

start=`date +%s`

export SCRAM_ARCH=slc6_amd64_gcc630
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

# -- CMSSW enviornment -- #
cd /cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_10_1_9 # -- has NNPDF3.1+luxQED PDF set
eval `scramv1 runtime -sh` # -- cmsenv

cd /home/kplee/Physics/FEWZ/v02_absRap/FEWZ_3.1.rc/bin

echo "run: ./local_run.sh z v20181001_TestForBinOpti_M1000to3000 v20181001_TestForBinOpti_M1000to3000_param.txt v20181001_TestForBinOpti_M1000to3000_hist.txt v20181001_TestForBinOpti_M1000to3000.dat ../ 24"
./local_run.sh z v20181001_TestForBinOpti_M1000to3000 v20181001_TestForBinOpti_M1000to3000_param.txt v20181001_TestForBinOpti_M1000to3000_hist.txt v20181001_TestForBinOpti_M1000to3000.dat ../ 24

echo "run: ./finish.sh v20181001_TestForBinOpti_M1000to3000 NNLO.v20181001_TestForBinOpti_M1000to3000.dat"
./finish.sh v20181001_TestForBinOpti_M1000to3000 NNLO.v20181001_TestForBinOpti_M1000to3000.dat

echo "job is completed"

end=`date +%s`

runtime=$((end-start))

echo "   start:   "$start
echo "   end:     "$end
echo "   runtime: "$runtime


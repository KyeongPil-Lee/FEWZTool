#!/bin/bash

export SCRAM_ARCH=slc6_amd64_gcc630
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

# -- CMSSW enviornment -- #
cd /cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_10_1_9 # -- has NNPDF3.1+luxQED PDF set
eval `scramv1 runtime -sh` # -- cmsenv

cd /home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc/bin

echo "run: ./local_run.sh z v20180923_XSecForDYSample_M15to50 v20180923_XSecForDYSample_M15to50_param.txt v20180923_XSecForDYSample_M15to50_hist.txt v20180923_XSecForDYSample_M15to50.dat ../ 24"
./local_run.sh z v20180923_XSecForDYSample_M15to50 v20180923_XSecForDYSample_M15to50_param.txt v20180923_XSecForDYSample_M15to50_hist.txt v20180923_XSecForDYSample_M15to50.dat ../ 24

echo "run: ./finish.sh v20180923_XSecForDYSample_M15to50 NNLO.v20180923_XSecForDYSample_M15to50.dat"
./finish.sh v20180923_XSecForDYSample_M15to50 NNLO.v20180923_XSecForDYSample_M15to50.dat

echo "job is completed"


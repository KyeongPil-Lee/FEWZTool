#!/bin/bash

start=`date +%s`

export SCRAM_ARCH=slc6_amd64_gcc630
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

# -- CMSSW enviornment -- #
cd /cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_10_1_9 # -- has NNPDF3.1+luxQED PDF set
eval `scramv1 runtime -sh` # -- cmsenv

cd /home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc/bin

# -- copy all necessary inputs under FEWZ/bin path
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v00_NNLOXSecForDYSample/v01_M50toInf/v20181207_XSecForDYSample_M50to10000_param.txt ./
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v00_NNLOXSecForDYSample/v01_M50toInf/v20181207_XSecForDYSample_M50to10000_hist.txt ./

echo "run local_run.sh"
./local_run.sh z \
v20181207_XSecForDYSample_M50to10000 \
v20181207_XSecForDYSample_M50to10000_param.txt \
v20181207_XSecForDYSample_M50to10000_hist.txt \
v20181207_XSecForDYSample_M50to10000.dat \
../ \
48

echo "run finish.sh"
./finish.sh \
v20181207_XSecForDYSample_M50to10000 \
NNLO.v20181207_XSecForDYSample_M50to10000.dat

# -- bring the output .dat file to Workspace
cp NNLO.v20181207_XSecForDYSample_M50to10000.dat /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v00_NNLOXSecForDYSample/v01_M50toInf

echo "job is completed"

end=`date +%s`

runtime=$((end-start))

echo "   start:   "$start
echo "   end:     "$end
echo "   runtime: "$runtime


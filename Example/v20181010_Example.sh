#!/bin/bash

start=`date +%s`

export SCRAM_ARCH=slc6_amd64_gcc630
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

# -- CMSSW enviornment -- #
cd /cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_10_1_9 # -- has NNPDF3.1+luxQED PDF set
eval `scramv1 runtime -sh` # -- cmsenv

cd /home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc//bin

# -- copy all necessary inputs under FEWZ/bin path
cp /data9/Users/kplee/FEWZTool/master/Example/v20181010_Example_param.txt ./
cp /data9/Users/kplee/FEWZTool/master/Example/v20181010_Example_hist.txt ./

echo "run local_run.sh"
./local_run.sh z \
v20181010_Example \
v20181010_Example_param.txt \
v20181010_Example_hist.txt \
v20181010_Example.dat \
../ \
24

echo "run finish.sh"
./finish.sh \
v20181010_Example \
NLO.v20181010_Example.dat

# -- bring the output .dat file to Workspace
cp NLO.v20181010_Example.dat /data9/Users/kplee/FEWZTool/master/Example

echo "job is completed"

end=`date +%s`

runtime=$((end-start))

echo "   start:   "$start
echo "   end:     "$end
echo "   runtime: "$runtime


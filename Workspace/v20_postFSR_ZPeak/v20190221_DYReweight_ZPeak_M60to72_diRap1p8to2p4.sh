#!/bin/bash

start=`date +%s`

export SCRAM_ARCH=slc6_amd64_gcc630
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

# -- CMSSW enviornment -- #
cd /cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_10_1_9 # -- has NNPDF3.1+luxQED PDF set
eval `scramv1 runtime -sh` # -- cmsenv

cd /home/kplee/Physics/FEWZ/v03_absRapCut/FEWZ_3.1.rc/bin

# -- copy all necessary inputs under FEWZ/bin path
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v20_postFSR_ZPeak/v20190221_DYReweight_ZPeak_M60to72_diRap1p8to2p4_param.txt ./
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v20_postFSR_ZPeak/v20190221_DYReweight_ZPeak_M60to72_diRap1p8to2p4_hist.txt ./
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v20_postFSR_ZPeak/binDiPt_ZPeak_v3.txt ./
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v20_postFSR_ZPeak/binDiRap_ZPeak_v3.txt ./

echo "run local_run.sh"
./local_run.sh z \
v20190221_DYReweight_ZPeak_M60to72_diRap1p8to2p4 \
v20190221_DYReweight_ZPeak_M60to72_diRap1p8to2p4_param.txt \
v20190221_DYReweight_ZPeak_M60to72_diRap1p8to2p4_hist.txt \
v20190221_DYReweight_ZPeak_M60to72_diRap1p8to2p4.dat \
../ \
12

echo "run finish.sh"
./finish.sh \
v20190221_DYReweight_ZPeak_M60to72_diRap1p8to2p4 \
NNLO.v20190221_DYReweight_ZPeak_M60to72_diRap1p8to2p4.dat

# -- bring the output .dat file to Workspace
cp NNLO.v20190221_DYReweight_ZPeak_M60to72_diRap1p8to2p4.dat /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v20_postFSR_ZPeak

echo "job is completed"

end=`date +%s`

runtime=$((end-start))

echo "   start:   "$start
echo "   end:     "$end
echo "   runtime: "$runtime


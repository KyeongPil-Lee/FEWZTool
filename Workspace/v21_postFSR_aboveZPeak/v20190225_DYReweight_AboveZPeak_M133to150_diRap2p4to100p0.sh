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
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v21_postFSR_aboveZPeak/v20190225_DYReweight_AboveZPeak_M133to150_diRap2p4to100p0_param.txt ./
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v21_postFSR_aboveZPeak/v20190225_DYReweight_AboveZPeak_M133to150_diRap2p4to100p0_hist.txt ./
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v21_postFSR_aboveZPeak/binDiPt_AboveZPeak_v3.txt ./
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v21_postFSR_aboveZPeak/binDiRap_AboveZPeak_v3.txt ./

echo "run local_run.sh"
./local_run.sh z \
v20190225_DYReweight_AboveZPeak_M133to150_diRap2p4to100p0 \
v20190225_DYReweight_AboveZPeak_M133to150_diRap2p4to100p0_param.txt \
v20190225_DYReweight_AboveZPeak_M133to150_diRap2p4to100p0_hist.txt \
v20190225_DYReweight_AboveZPeak_M133to150_diRap2p4to100p0.dat \
../ \
12

echo "run finish.sh"
./finish.sh \
v20190225_DYReweight_AboveZPeak_M133to150_diRap2p4to100p0 \
NNLO.v20190225_DYReweight_AboveZPeak_M133to150_diRap2p4to100p0.dat

# -- bring the output .dat file to Workspace
cp NNLO.v20190225_DYReweight_AboveZPeak_M133to150_diRap2p4to100p0.dat /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v21_postFSR_aboveZPeak

echo "job is completed"

end=`date +%s`

runtime=$((end-start))

echo "   start:   "$start
echo "   end:     "$end
echo "   runtime: "$runtime


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
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v15_3rdTrial_BelowZPeak/v20190212_DYReweight_BelowZPeak_M15to20_diRap1p5to2p4_NLO_param.txt ./
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v15_3rdTrial_BelowZPeak/v20190212_DYReweight_BelowZPeak_M15to20_diRap1p5to2p4_NLO_hist.txt ./
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v15_3rdTrial_BelowZPeak/binDiPt_belowZPeak_v3.txt ./
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v15_3rdTrial_BelowZPeak/binDiRap_belowZPeak_v3.txt ./

echo "run local_run.sh"
./local_run.sh z \
v20190212_DYReweight_BelowZPeak_M15to20_diRap1p5to2p4_NLO \
v20190212_DYReweight_BelowZPeak_M15to20_diRap1p5to2p4_NLO_param.txt \
v20190212_DYReweight_BelowZPeak_M15to20_diRap1p5to2p4_NLO_hist.txt \
v20190212_DYReweight_BelowZPeak_M15to20_diRap1p5to2p4_NLO.dat \
../ \
1

echo "run finish.sh"
./finish.sh \
v20190212_DYReweight_BelowZPeak_M15to20_diRap1p5to2p4_NLO \
NLO.v20190212_DYReweight_BelowZPeak_M15to20_diRap1p5to2p4_NLO.dat

# -- bring the output .dat file to Workspace
cp NLO.v20190212_DYReweight_BelowZPeak_M15to20_diRap1p5to2p4_NLO.dat /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v15_3rdTrial_BelowZPeak

echo "job is completed"

end=`date +%s`

runtime=$((end-start))

echo "   start:   "$start
echo "   end:     "$end
echo "   runtime: "$runtime


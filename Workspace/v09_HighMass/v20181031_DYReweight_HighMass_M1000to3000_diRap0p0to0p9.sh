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
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v09_HighMass/v20181031_DYReweight_HighMass_M1000to3000_diRap0p0to0p9_param.txt ./
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v09_HighMass/v20181031_DYReweight_HighMass_M1000to3000_diRap0p0to0p9_hist.txt ./
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v09_HighMass/binDiPt_HighMass_v1.txt ./
cp /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v09_HighMass/binDiRap_HighMass_v1.txt ./

echo "run local_run.sh"
./local_run.sh z \
v20181031_DYReweight_HighMass_M1000to3000_diRap0p0to0p9 \
v20181031_DYReweight_HighMass_M1000to3000_diRap0p0to0p9_param.txt \
v20181031_DYReweight_HighMass_M1000to3000_diRap0p0to0p9_hist.txt \
v20181031_DYReweight_HighMass_M1000to3000_diRap0p0to0p9.dat \
../ \
8

echo "run finish.sh"
./finish.sh \
v20181031_DYReweight_HighMass_M1000to3000_diRap0p0to0p9 \
NNLO.v20181031_DYReweight_HighMass_M1000to3000_diRap0p0to0p9.dat

# -- bring the output .dat file to Workspace
cp NNLO.v20181031_DYReweight_HighMass_M1000to3000_diRap0p0to0p9.dat /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v09_HighMass

echo "job is completed"

end=`date +%s`

runtime=$((end-start))

echo "   start:   "$start
echo "   end:     "$end
echo "   runtime: "$runtime


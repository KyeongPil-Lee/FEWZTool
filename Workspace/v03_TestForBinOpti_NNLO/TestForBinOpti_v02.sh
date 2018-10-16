#!/bin/bash

cd /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v03_TestForBinOpti_NNLO

# bash v20181007_TestForBinOpti_M15to60_diRap1p8to2p1.sh >&v20181007_TestForBinOpti_M15to60_diRap1p8to2p1.log
# echo "v20181007_TestForBinOpti_M15to60_diRap1p8to2p1.sh: finished"

bash v20181007_TestForBinOpti_M15to60_diRap2p1to2p4.sh >&v20181007_TestForBinOpti_M15to60_diRap2p1to2p4.log
echo "v20181007_TestForBinOpti_M15to60_diRap2p1to2p4.sh: finished"

bash v20181007_TestForBinOpti_M15to60_diRap2p4to100p0.sh >&v20181007_TestForBinOpti_M15to60_diRap2p4to100p0.log
echo "v20181007_TestForBinOpti_M15to60_diRap2p4to100p0.sh: finished"


echo "ALL: finished"

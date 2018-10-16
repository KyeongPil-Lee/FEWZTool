#!/bin/bash

cd /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v03_TestForBinOpti_NNLO

source v20181007_TestForBinOpti_M60to120_diRap0p0to0p3.sh >&v20181007_TestForBinOpti_M60to120_diRap0p0to0p3.log
echo "v20181007_TestForBinOpti_M60to120_diRap0p0to0p3.sh: finished"

source v20181007_TestForBinOpti_M60to120_diRap0p3to0p6.sh >&v20181007_TestForBinOpti_M60to120_diRap0p3to0p6.log
echo "v20181007_TestForBinOpti_M60to120_diRap0p3to0p6.sh: finished"

source v20181007_TestForBinOpti_M60to120_diRap0p6to0p9.sh >&v20181007_TestForBinOpti_M60to120_diRap0p6to0p9.log
echo "v20181007_TestForBinOpti_M60to120_diRap0p6to0p9.sh: finished"


echo "ALL: finished"

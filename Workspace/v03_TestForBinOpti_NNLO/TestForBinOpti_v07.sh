#!/bin/bash

cd /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v03_TestForBinOpti_NNLO

# bash v20181007_TestForBinOpti_M120to1000_diRap0p9to1p2.sh >&v20181007_TestForBinOpti_M120to1000_diRap0p9to1p2.log
# echo "v20181007_TestForBinOpti_M120to1000_diRap0p9to1p2.sh: finished"

bash v20181007_TestForBinOpti_M120to1000_diRap1p2to1p5.sh >&v20181007_TestForBinOpti_M120to1000_diRap1p2to1p5.log
echo "v20181007_TestForBinOpti_M120to1000_diRap1p2to1p5.sh: finished"

bash v20181007_TestForBinOpti_M120to1000_diRap1p5to1p8.sh >&v20181007_TestForBinOpti_M120to1000_diRap1p5to1p8.log
echo "v20181007_TestForBinOpti_M120to1000_diRap1p5to1p8.sh: finished"


echo "ALL: finished"
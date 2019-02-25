#!/bin/bash

cd /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v21_postFSR_aboveZPeak

bash v20190225_DYReweight_AboveZPeak_M133to150_diRap1p5to2p4.sh >&v20190225_DYReweight_AboveZPeak_M133to150_diRap1p5to2p4.log
echo "v20190225_DYReweight_AboveZPeak_M133to150_diRap1p5to2p4.sh: finished"

bash v20190225_DYReweight_AboveZPeak_M133to150_diRap2p4to100p0.sh >&v20190225_DYReweight_AboveZPeak_M133to150_diRap2p4to100p0.log
echo "v20190225_DYReweight_AboveZPeak_M133to150_diRap2p4to100p0.sh: finished"


echo "ALL: finished"

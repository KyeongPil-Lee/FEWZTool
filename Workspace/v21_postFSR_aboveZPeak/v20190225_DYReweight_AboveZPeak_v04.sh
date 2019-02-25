#!/bin/bash

cd /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v21_postFSR_aboveZPeak

bash v20190225_DYReweight_AboveZPeak_M150to171_diRap0p0to0p9.sh >&v20190225_DYReweight_AboveZPeak_M150to171_diRap0p0to0p9.log
echo "v20190225_DYReweight_AboveZPeak_M150to171_diRap0p0to0p9.sh: finished"

bash v20190225_DYReweight_AboveZPeak_M150to171_diRap0p9to1p5.sh >&v20190225_DYReweight_AboveZPeak_M150to171_diRap0p9to1p5.log
echo "v20190225_DYReweight_AboveZPeak_M150to171_diRap0p9to1p5.sh: finished"


echo "ALL: finished"

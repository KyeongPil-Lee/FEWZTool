#!/bin/bash

cd /data9/Users/kplee/FEWZTool/v01_Reweighting/Workspace/v17_3rdTrial_AboveZPeak

bash v20190212_DYReweight_AboveZPeak_M120to133_diRap0p0to0p9.sh >&v20190212_DYReweight_AboveZPeak_M120to133_diRap0p0to0p9.log
echo "v20190212_DYReweight_AboveZPeak_M120to133_diRap0p0to0p9.sh: finished"

bash v20190212_DYReweight_AboveZPeak_M120to133_diRap0p9to1p5.sh >&v20190212_DYReweight_AboveZPeak_M120to133_diRap0p9to1p5.log
echo "v20190212_DYReweight_AboveZPeak_M120to133_diRap0p9to1p5.sh: finished"


echo "ALL: finished"

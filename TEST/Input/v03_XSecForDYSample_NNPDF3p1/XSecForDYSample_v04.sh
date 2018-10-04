#!/bin/bash

cd /home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc/bin

source v20180923_XSecForDYSample_M1500to2000.sh >&v20180923_XSecForDYSample_M1500to2000.log
echo "v20180923_XSecForDYSample_M1500to2000.sh: finished"

source v20180923_XSecForDYSample_M2000to3000.sh >&v20180923_XSecForDYSample_M2000to3000.log
echo "v20180923_XSecForDYSample_M2000to3000.sh: finished"


echo "ALL: finished"

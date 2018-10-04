#!/bin/bash

cd /home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc/bin

source v20180923_XSecForDYSample_M10to50.sh >&v20180923_XSecForDYSample_M10to50.log
echo "v20180923_XSecForDYSample_M10to50.sh: finished"

source v20180923_XSecForDYSample_M15to50.sh >&v20180923_XSecForDYSample_M15to50.log
echo "v20180923_XSecForDYSample_M15to50.sh: finished"

source v20180923_XSecForDYSample_M50to100.sh >&v20180923_XSecForDYSample_M50to100.log
echo "v20180923_XSecForDYSample_M50to100.sh: finished"


echo "ALL: finished"

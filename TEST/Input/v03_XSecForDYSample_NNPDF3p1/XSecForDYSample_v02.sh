#!/bin/bash

cd /home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc/bin

source v20180923_XSecForDYSample_M200to400.sh >&v20180923_XSecForDYSample_M200to400.log
echo "v20180923_XSecForDYSample_M200to400.sh: finished"

source v20180923_XSecForDYSample_M400to500.sh >&v20180923_XSecForDYSample_M400to500.log
echo "v20180923_XSecForDYSample_M400to500.sh: finished"

source v20180923_XSecForDYSample_M500to700.sh >&v20180923_XSecForDYSample_M500to700.log
echo "v20180923_XSecForDYSample_M500to700.sh: finished"


echo "ALL: finished"

#!/bin/bash

cd /home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc/bin

source v20180923_XSecForDYSample_M50to200.sh >&v20180923_XSecForDYSample_M50to200.log
echo "v20180923_XSecForDYSample_M50to200.sh: finished"

source v20180923_XSecForDYSample_M50to10000.sh >&v20180923_XSecForDYSample_M50to10000.log
echo "v20180923_XSecForDYSample_M50to10000.sh: finished"

source v20180923_XSecForDYSample_M100to200.sh >&v20180923_XSecForDYSample_M100to200.log
echo "v20180923_XSecForDYSample_M100to200.sh: finished"


echo "ALL: finished"

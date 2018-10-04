#!/bin/bash

cd /home/kplee/Physics/FEWZ/LHAPDF_621/FEWZ_3.1.rc/bin

source v20180923_XSecForDYSample_M700to800.sh >&v20180923_XSecForDYSample_M700to800.log
echo "v20180923_XSecForDYSample_M700to800.sh: finished"

source v20180923_XSecForDYSample_M800to1000.sh >&v20180923_XSecForDYSample_M800to1000.log
echo "v20180923_XSecForDYSample_M800to1000.sh: finished"

source v20180923_XSecForDYSample_M1000to1500.sh >&v20180923_XSecForDYSample_M1000to1500.log
echo "v20180923_XSecForDYSample_M1000to1500.sh: finished"


echo "ALL: finished"

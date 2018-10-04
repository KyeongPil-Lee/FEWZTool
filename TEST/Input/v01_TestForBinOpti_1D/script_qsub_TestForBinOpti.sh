#!/bin/bash

qsub -l vnode=node7 v20180925_TestForBinOpti_M15to60.sh
qsub -l vnode=node7 v20180925_TestForBinOpti_M60to120.sh
qsub -l vnode=node8 v20180925_TestForBinOpti_M120to1000.sh
qsub -l vnode=node8 v20180925_TestForBinOpti_M1000to3000.sh

qsub -l vnode=node7 v20181001_TestForBinOpti_M15to60.sh
qsub -l vnode=node7 v20181001_TestForBinOpti_M60to120.sh
qsub -l vnode=node8 v20181001_TestForBinOpti_M120to1000.sh
qsub -l vnode=node8 v20181001_TestForBinOpti_M1000to3000.sh
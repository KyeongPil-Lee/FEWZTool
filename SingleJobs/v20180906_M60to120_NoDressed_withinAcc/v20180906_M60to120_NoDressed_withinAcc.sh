#!/bin/bash

#########################################################
# -- qsub commands: #$ + command (details: man qsub) -- #
#########################################################
# -- shell used for executing the script -- #
#$ -S /bin/sh

# -- combine standard output & error file -- #
#$ -j y

# -- send the mail when the job is aborted or ended -- #
#$ -m ae -M kplee@cern.ch

# -- stay in the directory where qsub command is executed -- #
#$ -cwd

cwd=$(pwd)

export SCRAM_ARCH=slc6_amd64_gcc530
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

# -- CMSSW enviornment -- #
cd /cvmfs/cms.cern.ch/slc6_amd64_gcc530/cms/cmssw/CMSSW_9_2_0
cmsenv

cd ${cwd}

echo "run: ./local_run.sh z v20180906_M60to120_NoDressed_withinAcc v20180906_M60to120_NoDressed_withinAcc_param.txt v20180906_M60to120_NoDressed_withinAcc_hist.txt v20180906_M60to120_NoDressed_withinAcc.dat ../ 40"
./local_run.sh z v20180906_M60to120_NoDressed_withinAcc v20180906_M60to120_NoDressed_withinAcc_param.txt v20180906_M60to120_NoDressed_withinAcc_hist.txt v20180906_M60to120_NoDressed_withinAcc.dat ../ 40

echo "run: ./finish.sh v20180906_M60to120_NoDressed_withinAcc NNLO.v20180906_M60to120_NoDressed_withinAcc.dat"
./finish.sh v20180906_M60to120_NoDressed_withinAcc NNLO.v20180906_M60to120_NoDressed_withinAcc.dat

echo "job is completed"

# -- &>log: "Invalid null command" Error occurs. please use >&log. -- #

# -- PLEASE ENTER AFTER THE LAST LINE! ... IF YOU DON'T, LAST LINE WILL NOT BE EXECUTED BY BATCH JOB -- # 

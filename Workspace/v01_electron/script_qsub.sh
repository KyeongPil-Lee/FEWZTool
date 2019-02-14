#!/bin/bash

qsub -l ncpus=24 v20190207_FiducialXSec_Zpeak_CT14nnlo_as_0118.sh
qsub -l ncpus=24 v20190207_FiducialXSec_Zpeak_NNPDF31_nnlo_as_0118_luxqed.sh
qsub -l ncpus=24 v20190211_FiducialXSec_Zpeak_CT14nnlo.sh
